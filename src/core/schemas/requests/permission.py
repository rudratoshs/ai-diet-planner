# src/core/schemas/requests/permission.py
from pydantic import BaseModel
from typing import Optional

class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(PermissionBase):
    name: Optional[str] = None