# src/db/migrations/versions/xxx_add_users_table.py
"""add users table

Revision ID: xxx
Revises: previous_revision_id
Create Date: 2025-02-08 13:40:00

"""
from alembic import op
import sqlalchemy as sa
from uuid import uuid4

revision = '1.0.0'
down_revision = '1a1c76a4521a'  # Replace with your previous revision ID
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(), nullable=False, default=uuid4),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

def downgrade() -> None:
    op.drop_table('users')