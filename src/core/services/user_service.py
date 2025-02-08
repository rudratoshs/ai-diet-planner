# src/core/services/user_service.py
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.user import User
from ..models.role import Role
from ..models.user_role import UserRole
from ..schemas.requests.user import UserCreate
from ...utils.security import get_password_hash

class UserService:
    @staticmethod
    async def create_user(db: Session, user_data: UserCreate):
        # Check if user exists
        if db.query(User).filter(User.email == user_data.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Create user
        db_user = User(
            email=user_data.email,
            hashed_password=get_password_hash(user_data.password)
        )
        db.add(db_user)
        try:
            db.commit()
            db.refresh(db_user)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        return db_user

    @staticmethod
    async def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    async def get_user_by_id(db: Session, user_id: UUID):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    async def get_user_roles(db: Session, user_id: UUID):
        return db.query(Role).join(UserRole).filter(
            UserRole.user_id == user_id
        ).all()