"""add is_protected to roles

Revision ID: e9ebea227e96
Revises: 1.0.0
Create Date: 2025-02-08 19:42:35.791178

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision: str = 'e9ebea227e96'
down_revision: Union[str, None] = '1.0.0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply the migration: Add is_protected column to roles"""
    op.add_column('roles', sa.Column('is_protected', sa.Boolean(), nullable=True))


def downgrade() -> None:
    """Rollback the migration: Remove is_protected column from roles"""
    op.drop_column('roles', 'is_protected')