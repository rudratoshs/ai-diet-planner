# src/core/models/permission.py
from sqlalchemy import Column, String, UUID
from uuid import uuid4
from .base import Base

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)