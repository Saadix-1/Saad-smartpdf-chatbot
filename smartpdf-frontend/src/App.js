import React, { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loadingUpload, setLoadingUpload] = useState(false);
  const [loadingAnswer, setLoadingAnswer] = useState(false);

  const BACKEND_URL = "http://127.0.0.1:5050";

  const uploadPDF = async () => {
    if (!file) return alert("Choisis un fichier PDF à uploader");
    setLoadingUpload(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(`${BACKEND_URL}/upload`, {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      alert(data.message || data.error);
    } catch (error) {
      alert("Erreur upload : " + error.message);
    }

    setLoadingUpload(false);
  };

  const askQuestion = async () => {
    if (!question.trim()) return alert("Pose une question");
    setLoadingAnswer(true);

    try {
      const res = await fetch(`${BACKEND_URL}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setAnswer(data.response || data.error);
    } catch (error) {
      setAnswer("Erreur : " + error.message);
    }

    setLoadingAnswer(false);
  };

  return (
    <div className="container">
      <h1> Saad's SmartPDF Chatbot</h1>

      {/* Upload Section */}
      <div className="card">
        <h2>Uploader un PDF</h2>
        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => setFile(e.target.files[0])}
          disabled={loadingUpload}
        />
        <button onClick={uploadPDF} disabled={loadingUpload}>
          {loadingUpload ? "Upload en cours..." : "Uploader"}
        </button>
      </div>

      {/* Question Section */}
      <div className="card">
        <h2>Poser une question</h2>
        <textarea
          rows={4}
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Tape ta question ici..."
          disabled={loadingAnswer}
        />
        <button onClick={askQuestion} disabled={loadingAnswer || !question.trim()}>
          {loadingAnswer ? "En cours..." : "Envoyer"}
        </button>

        <div className="response">
          {answer || "La réponse s’affichera ici:"}
        </div>
      </div>
    </div>
  );
}

export default App;
