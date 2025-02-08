# src/core/schemas/requests/assignment.py
from pydantic import BaseModel
from uuid import UUID

class RoleAssignmentCreate(BaseModel):
    user_id: UUID
    role_id: UUID
    expires_at: str | None = None

class RoleAssignmentDelete(BaseModel):
    user_id: UUID
    role_id: UUID