# src/core/schemas/requests/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str

    @classmethod
    def from_orm(cls, obj):
        return cls(id=str(obj.id), email=obj.email)

    class Config:
        from_attributes = True