"""create posts table

Revision ID: ff1d8d269729
Revises: 
Create Date: 2022-09-29 15:35:08.585956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff1d8d269729'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(255), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
