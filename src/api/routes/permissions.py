# src/api/routes/permissions.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...core.services.permission_service import PermissionService
from ...core.schemas.requests.permission import PermissionCreate, PermissionUpdate
from uuid import UUID

router = APIRouter(prefix="/permissions", tags=["permissions"])

@router.post("/", status_code=201)
async def create_permission(
    permission_data: PermissionCreate,
    db: Session = Depends(get_db)
):
    return await PermissionService.create_permission(db, permission_data)

@router.get("/{permission_id}")
async def get_permission(
    permission_id: UUID,
    db: Session = Depends(get_db)
):
    return await PermissionService.get_permission(db, permission_id)