"""add columns to posts table

Revision ID: 8142b9e271a5
Revises: 48c18cb07349
Create Date: 2023-05-09 14:03:42.936981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8142b9e271a5'
down_revision = '48c18cb07349'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
