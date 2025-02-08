# tests/unit/test_role_service.py
import pytest
from uuid import uuid4
from src.core.services.role_service import RoleService
from src.core.schemas.requests.role import RoleCreate

@pytest.mark.asyncio
async def test_create_role(db_session):
    role_data = RoleCreate(
        name="test_role",
        description="Test role description"
    )
    
    role = await RoleService.create_role(db_session, role_data)
    assert role.name == "test_role"
    assert role.description == "Test role description"