from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class ExecutionRequest(BaseModel):
    input: Dict[str, Any] = Field(..., description="Input payload for workflow")


class ExecutionResponse(BaseModel):
    status: str
    data: Dict[str, Any]


class ExecutionCreate(BaseModel):
    agent_name: str
    input: Dict[str, Any]


class ExecutionRecord(BaseModel):
    id: int
    agent_name: str
    input: Dict[str, Any]
    output: Dict[str, Any]
    status: str
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


class ExecutionListResponse(BaseModel):
    executions: list[ExecutionRecord]