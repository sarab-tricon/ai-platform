from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from db.session import Base


# ------------------ USER ------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)




# ------------------ WORKFLOW ------------------
class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


# ------------------ EXECUTION ------------------
class Sessions(Base):
    __tablename__ = "sessions"

    session_id = Column(Integer, primary_key=True, index=True)

    workflow_id = Column(Integer, ForeignKey("workflows.id"))

    response = Column(Text, nullable=True)
    response_type = Column()
    created_at = Column(DateTime, default=datetime.utcnow)

    workflow = relationship("Workflow", back_populates="executions")