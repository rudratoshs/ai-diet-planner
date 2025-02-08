# src/core/schemas/requests/role.py
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List

class RoleCreate(BaseModel):
    name: str
    description: Optional[str] = None
    permission_ids: Optional[List[UUID]] = []

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    permission_ids: Optional[List[UUID]] = None