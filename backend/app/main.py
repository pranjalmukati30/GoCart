from fastapi import FastAPI
from pydantic import BaseModel
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    description="Backend API for GoCart e-commerce platform",
    version=settings.app_version
)


@app.get("/health")
def health():
    return {
        "status" : "running"
    }