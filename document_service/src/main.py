import logging

from fastapi import FastAPI
from .routers import upload, status

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(upload.router)
app.include_router(status.router)


@app.get("/health")
async def health_check():
    # Perform and return the health check results
    return {"status": "healthy"}
