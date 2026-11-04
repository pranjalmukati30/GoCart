from fastapi import FastAPI
from app.config import settings
from app.routers.auth import router as auth_router

app = FastAPI(
    title=settings.app_name,
    description="Backend API for GoCart e-commerce platform",
    version=settings.app_version
)

app.include_router(auth_router)

@app.get("/health")
def health():
    return {
        "status" : "running"
    }