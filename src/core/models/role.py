# src/core/models/role.py
from sqlalchemy import Column, String, UUID, ForeignKey, Table,Boolean
from sqlalchemy.orm import relationship
from uuid import uuid4
from .base import Base

role_permissions = Table(
    'role_permissions',
    Base.metadata,
    Column('role_id', UUID, ForeignKey('roles.id')),
    Column('permission_id', UUID, ForeignKey('permissions.id'))
)

class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    permissions = relationship("Permission", secondary=role_permissions)
    is_protected = Column(Boolean, default=False)