from fastapi import FastAPI
from .routers import upload

app = FastAPI()

app.include_router(upload.router)


@app.get("/health")
async def health_check():
    # Perform and return the health check results
    return {"status": "healthy"}
