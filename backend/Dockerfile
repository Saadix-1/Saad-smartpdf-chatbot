FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy React build into the container (if it exists)
COPY frontend_dist/ /app/frontend_dist/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
