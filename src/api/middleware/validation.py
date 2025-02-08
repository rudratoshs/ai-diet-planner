# src/api/middleware/validation.py
from fastapi import Request, HTTPException
from typing import List, Optional

class RoleValidationMiddleware:
    def __init__(self, required_roles: List[str]):
        self.required_roles = required_roles

    async def __call__(self, request: Request):
        user = request.state.user
        if not user:
            raise HTTPException(status_code=403, detail="Not authenticated")
        
        user_roles = user.get("roles", [])
        if not any(role in user_roles for role in self.required_roles):
            raise HTTPException(status_code=403, detail="Insufficient permissions")