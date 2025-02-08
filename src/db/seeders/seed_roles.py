from sqlalchemy.orm import Session
from src.core.models.role import Role
from src.core.models.user_role import UserRole
from src.core.models.user import User
from src.core.models.permission import Permission
from src.db.seeders.seed_permissions import seed_permissions
from src.utils.security import get_password_hash
from uuid import uuid4
from sqlalchemy.sql import text

def seed_roles(db: Session):
    """Seed roles and ensure permissions exist before assigning."""

    # Ensure permissions are seeded first
    seed_permissions(db)

    # Create the Super Admin role if it does not exist
    super_admin_role = db.query(Role).filter(Role.name == "super_admin").first()
    if not super_admin_role:
        super_admin_role = Role(
            id=uuid4(),
            name="super_admin",
            description="Super Administrator with all permissions",
            is_protected=True  # Prevent deletion
        )
        db.add(super_admin_role)

    # Create an Admin role if it does not exist
    admin_role = db.query(Role).filter(Role.name == "admin").first()
    if not admin_role:
        admin_role = Role(
            id=uuid4(),
            name="admin",
            description="Administrator with elevated privileges",
            is_protected=False
        )
        db.add(admin_role)

    db.commit()

    # Assign all permissions to Super Admin
    permissions = db.query(Permission).all()
    for perm in permissions:
        db.execute(
            text("INSERT INTO role_permissions (role_id, permission_id) VALUES (:role_id, :perm_id) "
                "ON CONFLICT DO NOTHING"),
            {"role_id": str(super_admin_role.id), "perm_id": str(perm.id)}
        )

    db.commit()

    # Create a default Super Admin user if not exists
    admin_email = "rudra@planner.com"
    existing_admin = db.query(User).filter(User.email == admin_email).first()
    if not existing_admin:
        super_admin_user = User(
            id=uuid4(),
            email=admin_email,
            hashed_password=get_password_hash("admin123"),
        )
        db.add(super_admin_user)
        db.commit()
        db.refresh(super_admin_user)

        # Assign Super Admin role
        db.execute(
            text("INSERT INTO user_roles (user_id, role_id) VALUES (:user_id, :role_id) "
                "ON CONFLICT DO NOTHING"),
            {"user_id": str(super_admin_user.id), "role_id": str(super_admin_role.id)}
        )

        db.commit()