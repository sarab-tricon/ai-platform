from pydantic import BaseModel
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class WorkflowResponse(BaseModel):
    name: str
    description: Optional[str] = None


class WorkflowListResponse(BaseModel):
    workflows: List[str]


class WorkflowDetailResponse(BaseModel):
    name: str
    nodes: Optional[List[str]] = None
    description: Optional[str] = None