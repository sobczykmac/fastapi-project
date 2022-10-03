"""add foreign key to post table

Revision ID: 5fef8e4c55a5
Revises: 7c7a054c30ec
Create Date: 2022-09-29 18:18:59.682671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fef8e4c55a5'
down_revision = '7c7a054c30ec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"],
                          remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts", type_="foreignkey")
    op.drop_column("posts", "owner_id")
    pass
