# src/core/models/user_role.py
from sqlalchemy import Column, ForeignKey, UUID, DateTime
from uuid import uuid4
from .base import Base

class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(UUID, primary_key=True, default=uuid4)
    user_id = Column(UUID, nullable=False)
    role_id = Column(UUID, ForeignKey('roles.id'), nullable=False)
    expires_at = Column(DateTime, nullable=True)

    class Config:
        orm_mode = True