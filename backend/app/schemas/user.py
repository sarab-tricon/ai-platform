from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: Optional[EmailStr]