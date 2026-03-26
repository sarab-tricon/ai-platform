from fastapi import APIRouter, HTTPException
from app.services.workflow import workflow_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/workflows", tags=["Workflows"])


@router.get("")
async def list_workflows():
    logger.info("Listing workflows")

    try:
        return {"workflows": workflow_service.list_workflows()}
    except Exception as e:
        logger.error(f"Workflow listing failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{name}")
async def get_workflow(name: str):
    logger.info(f"Fetching workflow: {name}")

    try:
        return workflow_service.get_workflow(name)
    except Exception as e:
        logger.error(f"Workflow fetch failed: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))