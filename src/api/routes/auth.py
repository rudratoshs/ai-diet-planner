# src/api/routes/auth.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...core.schemas.requests.auth import LoginRequest
from ...core.schemas.requests.user import UserCreate, UserResponse
from ...utils.security import create_jwt, verify_password
from ...core.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", response_model=UserResponse)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = await UserService.create_user(db, user_data)
    return UserResponse.from_orm(new_user)

@router.post("/login")
async def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = await UserService.get_user_by_email(db, login_data.email)
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )
    # Get user roles
    roles = await UserService.get_user_roles(db, user.id)
    # Create token
    token = create_jwt({
        "sub": str(user.id),
        "email": user.email,
        "roles": [role.name for role in roles]
    })
    return {
        "access_token": token,
        "token_type": "bearer"
    }