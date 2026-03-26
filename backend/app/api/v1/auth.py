from fastapi import APIRouter, HTTPException
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth import auth_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    logger.info("Login request received")

    try:
        return auth_service.login(request.email, request.password)
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))