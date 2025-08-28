from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import faiss
import numpy as np
import json

from sentence_transformers import SentenceTransformer
from llm_interface.query_ollama import query_ollama
from scripts.extract_pdf import extract_text_from_pdf  
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "data"
ALLOWED_EXTENSIONS = {"pdf"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

#  Utilitaires
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

model = SentenceTransformer("all-MiniLM-L6-v2")

#  Route 1 — Upload PDF
@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier fourni"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Nom de fichier vide"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        print(f"[LOG] Fichier enregistré sous : {filepath}")

        # Extraction
        text = extract_text_from_pdf(filepath)
        with open("data/extracted_text.json", "w", encoding="utf-8") as f:
            json.dump({"text": text}, f)

        # Chunk + embeddings + save FAISS
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        embeddings = model.encode(chunks).astype("float32")
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        faiss.write_index(index, "db/faiss_index/index.faiss")

        with open("db/faiss_index/chunks.json", "w", encoding="utf-8") as f:
            json.dump(chunks, f)

        return jsonify({"message": " PDF traité avec succès"}), 200
    return jsonify({"error": "Fichier non supporté"}), 400

#  Route 2 — Poser une question
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Question vide"}), 400

    # Charger FAISS + chunks
    index = faiss.read_index("db/faiss_index/index.faiss")
    with open("db/faiss_index/chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)

    question_embedding = model.encode([question]).astype("float32")
    D, I = index.search(question_embedding, 5)
    context_chunks = [chunks[i] for i in I[0] if 0 <= i < len(chunks)]

    context_text = "\n\n".join(context_chunks)
    prompt = f"Voici le contexte :\n{context_text}\n\nQuestion: {question}\nRéponse :"
    response = query_ollama(prompt)

    return jsonify({"response": response})
