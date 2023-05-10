"""add columns to posts table

Revision ID: 3c1caeab8481
Revises: 5a51693b5e14
Create Date: 2023-05-10 10:13:00.879101

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '3c1caeab8481'
down_revision = '5a51693b5e14'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')))
    op.add_column('posts', sa.Column('privated', sa.Boolean(),
                  nullable=False, server_default="TRUE"))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'private')
    op.drop_column('posts', 'created_at')
    pass
