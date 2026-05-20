# Saad AI — Smart PDF Chatbot 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pinecone&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

> **🚀 Live Demo:** [https://d2ehw7ojcpifbu.cloudfront.net/](https://d2ehw7ojcpifbu.cloudfront.net/)

---

**Saad AI** is a cloud-native, RAG-based chatbot application that leverages advanced NLP techniques and large language models (LLMs) to let users upload any PDF document and interact with its content through a natural-language interface.

Re-architected from local LLMs to a fully cloud-native deployment model using **OpenAI** and **Pinecone**, this project demonstrates expertise in building scalable, enterprise-ready AI backends and modern React frontends — deployed end-to-end on **AWS** (EC2 + CloudFront).

---

## ✨ Features

- **RAG Pipeline (Retrieval-Augmented Generation):** Extracts text from PDFs, embeds it into a Pinecone vector index, and retrieves the most relevant chunks at query time for accurate, context-aware responses.
- **Cloud-Native & Stateless Processing:** Processes uploaded PDF files directly via memory streams — no local disk persistence required, making it portable across any containerized infrastructure.
- **Managed Vector Database:** Uses **Pinecone** for fast and reliable semantic similarity search without maintaining local FAISS indices.
- **State-of-the-Art LLMs:** Powered by OpenAI's `gpt-3.5-turbo` for intelligent responses and `text-embedding-3-small` for dense vector embeddings.
- **Modern React Frontend:** A sleek, responsive UI built with **React 18**, **Vite**, and **Tailwind CSS** for a fluid, real-time chat experience.
- **Production Deployment on AWS:** Frontend served via **AWS CloudFront** CDN; backend running on an **AWS EC2** instance inside a Docker container. 

---

## 🛠️ Technologies Used

### Backend
| Technology | Purpose |
|---|---|
| **FastAPI** | Asynchronous REST API framework |
| **Pinecone** | Managed vector database for semantic search |
| **OpenAI API** | Embeddings (`text-embedding-3-small`) & chat (`gpt-3.5-turbo`) |
| **PyMuPDF (fitz)** | Rapid, accurate PDF text extraction |
| **Docker** | Containerized deployment |

### Frontend
| Technology | Purpose |
|---|---|
| **React 18 & Vite** | High-performance UI and dev tooling |
| **Tailwind CSS** | Utility-first responsive styling |
| **Lucide Icons** | SVG-based interface iconography |

### Cloud Infrastructure
| Service | Role |
|---|---|
| **AWS EC2** | Hosts the FastAPI backend Docker container |
| **AWS CloudFront** | CDN serving the React frontend globally |
| **AWS SSM Parameter Store** | Secure secret management for API keys |

---
 
## 📂 Project Structure

```
smartpdf-chatbot/
├── backend/
│   ├── app/
│   │   ├── main.py          # Application entry point
│   │   ├── api/             # REST Endpoints (upload, chat)
│   │   ├── core/            # Configuration and Application State
│   │   └── services/        # Business Logic (Pinecone, OpenAI, PDF Extraction)
│   ├── requirements.txt     # Python Dependencies
│   └── .env.example         # Template for required cloud API keys
├── frontend/
│   ├── src/
│   │   ├── App.tsx          # Main React web UI interface
│   │   ├── components/      # Reusable React components
│   │   └── index.css        # Global Tailwind CSS definitions
│   ├── package.json         # Node Dependencies
│   └── vite.config.ts       # Vite Bundler Configuration
├── docker-compose.yml       # Container deployment manifest
└── README.md
```

---

## 🚀 Getting Started Locally

To run Saad AI locally, you will need active API keys from OpenAI and Pinecone.

### Prerequisites

- Node.js v20+
- Python 3.10+
- An [OpenAI](https://platform.openai.com/) Developer Account & API Key
- A [Pinecone](https://www.pinecone.io/) Account & API Key (Free Tier supported)

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Saadix-1/Saad-smartpdf-chatbot.git
   cd Saad-smartpdf-chatbot/backend
   ```

2. **Create your environment configuration file:**
   ```bash
   cp .env.example .env
   ```

3. **Open `.env` and add your API credentials:**
   ```env
   OPENAI_API_KEY=sk-proj-your_openai_api_key_here
   PINECONE_API_KEY=pcsk_your_pinecone_api_key_here
   PINECONE_INDEX_NAME=smartpdf-index
   ```

4. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Run the backend server:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the Vite dev server:**
   ```bash
   npm run dev
   ```

4. Open your browser at [http://localhost:5173](http://localhost:5173). Upload a PDF and start chatting!

---

## ☁️ Cloud Deployment (AWS)

This project is deployed end-to-end on AWS:

### Backend — AWS EC2 + Docker
- The FastAPI backend is containerized using Docker and runs on an **AWS EC2** instance.
- API keys are securely injected at runtime using **AWS SSM Parameter Store**.
- The backend serves both the API and the built frontend static files from a single unified host.

### Frontend — AWS CloudFront
- The React frontend is built (`npm run build`) and served globally via an **AWS CloudFront** distribution.
- Live URL: [https://d2ehw7ojcpifbu.cloudfront.net/](https://d2ehw7ojcpifbu.cloudfront.net/)

### Alternative Hosting Options
- **Frontend:** Deploy `/dist` to Vercel, Netlify, or Firebase Hosting.
- **Backend:** Package with Docker and deploy to **Google Cloud Run**, **AWS App Runner**, or **AWS Fargate** for serverless container hosting.

---

## 💡 Why This Project Stands Out

- **Production-Ready Architecture:** Shifted from a local monolithic setup to a cloud-native microservice architecture using fully managed services.
- **Stateless Engineering:** PDFs and embeddings are processed strictly in memory and over APIs — no persistent disk or local database required.
- **Real AWS Deployment:** Not just a demo — this is a live application deployed end-to-end on AWS infrastructure with proper secret management.
- **Modern AI Techniques:** Built on leading enterprise-grade models (OpenAI) and managed vector infrastructure (Pinecone), showcasing real-world RAG implementation skills.
- **Beautiful User Interface:** A bespoke, premium dark-mode UI with fluid animations and responsive design.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, feel free to fork the repository and submit a pull request.
