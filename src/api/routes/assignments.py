# src/api/routes/assignments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...core.services.assignment_service import AssignmentService
from ...core.schemas.requests.assignment import RoleAssignmentCreate, RoleAssignmentDelete
from uuid import UUID

router = APIRouter(prefix="/assignments", tags=["assignments"])

@router.post("/", status_code=201)
async def assign_role(
    assignment_data: RoleAssignmentCreate,
    db: Session = Depends(get_db)
):
    return await AssignmentService.assign_role(db, assignment_data)

@router.delete("/")
async def remove_role_assignment(
    assignment_data: RoleAssignmentDelete,
    db: Session = Depends(get_db)
):
    return await AssignmentService.remove_role_assignment(db, assignment_data)

@router.get("/user/{user_id}")
async def get_user_roles(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    return await AssignmentService.get_user_roles(db, user_id)