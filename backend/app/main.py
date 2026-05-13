from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .core.config import settings
from .api import endpoints
import os

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints.router, prefix=settings.API_V1_STR)

@app.get("/health")
def health():
    return {"message": "Saad AI Backend is running"}

# Serve React frontend static files (if dist folder exists)
static_dir = os.path.join(os.path.dirname(__file__), "../frontend_dist")
if os.path.exists(static_dir):
    app.mount("/assets", StaticFiles(directory=os.path.join(static_dir, "assets")), name="assets")

    @app.get("/")
    def serve_frontend():
        return FileResponse(os.path.join(static_dir, "index.html"))

    @app.get("/{catchall:path}")
    def serve_spa(catchall: str):
        index = os.path.join(static_dir, "index.html")
        return FileResponse(index)
else:
    @app.get("/")
    def read_root():
        return {"message": "Saad AI Backend is running"}
