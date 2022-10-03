"""add user table

Revision ID: 7c7a054c30ec
Revises: 107784659386
Create Date: 2022-09-29 18:07:43.214866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c7a054c30ec'
down_revision = '107784659386'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(255), nullable=False),
                    sa.Column("password", sa.String(255), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"),nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))
    pass


def downgrade():
    op.drop_table("users")
    pass
