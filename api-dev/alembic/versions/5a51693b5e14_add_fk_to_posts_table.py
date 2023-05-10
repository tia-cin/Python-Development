"""add fk to posts table

Revision ID: 5a51693b5e14
Revises: 01c25bde9381
Create Date: 2023-05-10 10:07:20.201231

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '5a51693b5e14'
down_revision = '01c25bde9381'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id',  UUID(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column(('posts'), 'owner_id')
    pass
