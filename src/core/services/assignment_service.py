# src/core/services/assignment_service.py
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.role import Role
from ..models.user_role import UserRole
from ..schemas.requests.assignment import RoleAssignmentCreate, RoleAssignmentDelete

class AssignmentService:
    @staticmethod
    async def assign_role(db: Session, assignment_data: RoleAssignmentCreate):
        # Check if role exists
        role = db.query(Role).filter(Role.id == assignment_data.role_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")

        # Check if assignment already exists
        existing_assignment = db.query(UserRole).filter(
            UserRole.user_id == assignment_data.user_id,
            UserRole.role_id == assignment_data.role_id
        ).first()

        if existing_assignment:
            raise HTTPException(status_code=400, detail="Role already assigned to user")

        # Create new assignment
        user_role = UserRole(
            user_id=assignment_data.user_id,
            role_id=assignment_data.role_id,
            expires_at=assignment_data.expires_at
        )
        
        db.add(user_role)
        try:
            db.commit()
            db.refresh(user_role)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        
        return user_role

    @staticmethod
    async def remove_role_assignment(db: Session, assignment_data: RoleAssignmentDelete):
        assignment = db.query(UserRole).filter(
            UserRole.user_id == assignment_data.user_id,
            UserRole.role_id == assignment_data.role_id
        ).first()

        if not assignment:
            raise HTTPException(status_code=404, detail="Role assignment not found")

        try:
            db.delete(assignment)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e))

        return {"message": "Role assignment removed successfully"}

    @staticmethod
    async def get_user_roles(db: Session, user_id: UUID):
        roles = db.query(Role).join(UserRole).filter(
            UserRole.user_id == user_id
        ).all()
        
        return roles