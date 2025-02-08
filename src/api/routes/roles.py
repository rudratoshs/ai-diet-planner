# src/api/routes/roles.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...core.services.role_service import RoleService
from ...core.schemas.requests.role import RoleCreate, RoleUpdate
from ..middleware.auth import get_current_user
from typing import List
from uuid import UUID
from ...core.models.role import Role
from uuid import uuid4
from pydantic import BaseModel

router = APIRouter(prefix="/roles", tags=["roles"])

# Define Pydantic schema for request body
class RoleCreate(BaseModel):
    name: str
    description: str
    is_protected: bool = False

@router.post("/", status_code=201)
def create_role(
    role_data: RoleCreate,  # ✅ Accept request body as Pydantic model
    db: Session = Depends(get_db)
):
    # Check if role already exists
    existing_role = db.query(Role).filter(Role.name == role_data.name).first()
    if existing_role:
        raise HTTPException(status_code=400, detail=f"Role '{role_data.name}' already exists.")

    # Insert new role
    new_role = Role(
        id=uuid4(),
        name=role_data.name,
        description=role_data.description,
        is_protected=role_data.is_protected
    )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role

@router.get("/{role_id}")
async def get_role(
    role_id: UUID,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await RoleService.get_role(db, role_id)