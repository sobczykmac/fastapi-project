"""add last few columns to posts table

Revision ID: 755a44d60420
Revises: 5fef8e4c55a5
Create Date: 2022-09-29 18:26:29.387300

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '755a44d60420'
down_revision = '5fef8e4c55a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default='1'))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                     server_default=sa.text("now()"), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
    pass
