from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.execution import router as execution_router
from app.api.v1.workflow import router as workflow_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(execution_router)
api_router.include_router(workflow_router)