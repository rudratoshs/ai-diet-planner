from sqlalchemy.orm import Session
from src.core.models.permission import Permission
from uuid import uuid4

def seed_permissions(db: Session):
    """Seed the database with default permissions."""

    permissions_list = [
        "create_user", "delete_user", "update_user", "view_users",
        "create_role", "delete_role", "update_role", "view_roles",
        "assign_role", "remove_role",
        "manage_permissions"
    ]

    for perm_name in permissions_list:
        existing_perm = db.query(Permission).filter(Permission.name == perm_name).first()
        if not existing_perm:
            db.add(Permission(id=uuid4(), name=perm_name, description=f"Permission to {perm_name.replace('_', ' ')}"))

    db.commit()