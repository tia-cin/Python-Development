"""change id column from posts table

Revision ID: b561989b1c84
Revises: 3c1caeab8481
Create Date: 2023-05-10 10:35:26.700294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b561989b1c84'
down_revision = '3c1caeab8481'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('posts', 'id', server_default=sa.text("gen_random_uuid()"))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'id')
    pass
