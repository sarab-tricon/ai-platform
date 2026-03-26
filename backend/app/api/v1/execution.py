from fastapi import APIRouter, HTTPException
from app.schemas.execution import ExecutionRequest, ExecutionResponse
from app.services.execution import execution_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agents", tags=["Agents"])


@router.post("/execute/{agent_name}", response_model=ExecutionResponse)
async def run_agent(agent_name: str, request: ExecutionRequest):
    logger.info(f"Executing agent: {agent_name}")

    try:
        return execution_service.run_agent(agent_name, request.input)
    except Exception as e:
        logger.error(f"Execution failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))