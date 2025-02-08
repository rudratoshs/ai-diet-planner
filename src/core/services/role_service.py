# src/core/services/role_service.py
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.role import Role
from ..schemas.requests.role import RoleCreate, RoleUpdate

class RoleService:
    @staticmethod
    async def create_role(db: Session, role_data: RoleCreate):
        db_role = Role(
            name=role_data.name,
            description=role_data.description
        )
        db.add(db_role)
        try:
            db.commit()
            db.refresh(db_role)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        return db_role

    @staticmethod
    async def get_role(db: Session, role_id: UUID):
        role = db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role