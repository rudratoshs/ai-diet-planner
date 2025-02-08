# src/core/models/user.py
from sqlalchemy import Column, String, UUID, DateTime
from uuid import uuid4
from datetime import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, default=uuid4)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)