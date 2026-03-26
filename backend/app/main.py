from fastapi import FastAPI
from app.api.v1 import api_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Agentic AI Platform",
    version="1.0.0"
)

app.include_router(api_router)


@app.get("/health")
async def health():
    logger.info("Health check called")
    return {"status": "ok"}