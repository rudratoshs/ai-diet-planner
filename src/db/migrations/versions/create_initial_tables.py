# src/db/migrations/versions/create_initial_tables.py
"""create initial tables

Revision ID: 1a1c76a4521a
Revises: 
Create Date: 2025-02-08 13:30:00

"""
from alembic import op
import sqlalchemy as sa
from uuid import uuid4

# revision identifiers, used by Alembic.
revision = '1a1c76a4521a'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.UUID(), nullable=False, default=uuid4),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Create permissions table
    op.create_table(
        'permissions',
        sa.Column('id', sa.UUID(), nullable=False, default=uuid4),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Create role_permissions table
    op.create_table(
        'role_permissions',
        sa.Column('role_id', sa.UUID(), nullable=False),
        sa.Column('permission_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('role_id', 'permission_id')
    )

    # Create user_roles table
    op.create_table(
        'user_roles',
        sa.Column('id', sa.UUID(), nullable=False, default=uuid4),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('role_id', sa.UUID(), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('user_roles')
    op.drop_table('role_permissions')
    op.drop_table('permissions')
    op.drop_table('roles')