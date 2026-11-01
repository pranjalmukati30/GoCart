from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="GoCart API",
    description="Backend API for GoCart e-commerce platform",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status" : "running"
    }