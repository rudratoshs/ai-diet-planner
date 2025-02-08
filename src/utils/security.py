# src/utils/security.py
import jwt as PyJWT  # Explicit import
from datetime import datetime, timedelta
from passlib.context import CryptContext
from ..config.environment import env

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_jwt(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    return PyJWT.encode(
        to_encode,
        env.JWT_SECRET_KEY,
        algorithm=env.JWT_ALGORITHM
    )

def decode_jwt(token: str) -> dict:
    return PyJWT.decode(
        token,
        env.JWT_SECRET_KEY,
        algorithms=[env.JWT_ALGORITHM]
    )

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)