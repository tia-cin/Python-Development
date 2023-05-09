"""add user table

Revision ID: 01c25bde9381
Revises: 8142b9e271a5
Create Date: 2023-05-09 14:08:26.517004

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '01c25bde9381'
down_revision = '8142b9e271a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', UUID(), nullable=False,
                              server_default=sa.text('gen_random_uuid()')),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
