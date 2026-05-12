# Testing the SmartPDF Chatbot Locally

Whenever you want to run the chatbot in the future, follow these two simple steps to start the servers. You will need two separate terminal windows.

## 1. Start the Backend API
In your first terminal, navigate to the backend folder and start the server:

```bash
cd /Users/saadmehamdi/Documents/Saadpdf-chatbot-main/backend
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
*You'll know it's working when you see `Uvicorn running on http://0.0.0.0:8000`.*

---

## 2. Start the Frontend UI
In your second terminal, navigate to the frontend folder and start the React app:

```bash
cd /Users/saadmehamdi/Documents/Saadpdf-chatbot-main/frontend
npm run dev
```
*You'll know it's working when you see `VITE ready` and `http://localhost:5173`.*

---

## 3. Use the App!
Open your web browser and go to your frontend link:
👉 **[http://localhost:5173](http://localhost:5173)**
