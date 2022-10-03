"""add content column to post table

Revision ID: 107784659386
Revises: ff1d8d269729
Create Date: 2022-09-29 15:42:42.641803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107784659386'
down_revision = 'ff1d8d269729'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(255), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
