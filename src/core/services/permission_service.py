# src/core/services/permission_service.py
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.permission import Permission
from ..schemas.requests.permission import PermissionCreate, PermissionUpdate

class PermissionService:
    @staticmethod
    async def create_permission(db: Session, permission_data: PermissionCreate):
        db_permission = Permission(
            name=permission_data.name,
            description=permission_data.description
        )
        db.add(db_permission)
        try:
            db.commit()
            db.refresh(db_permission)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        return db_permission

    @staticmethod
    async def get_permission(db: Session, permission_id: UUID):
        permission = db.query(Permission).filter(Permission.id == permission_id).first()
        if not permission:
            raise HTTPException(status_code=404, detail="Permission not found")
        return permission