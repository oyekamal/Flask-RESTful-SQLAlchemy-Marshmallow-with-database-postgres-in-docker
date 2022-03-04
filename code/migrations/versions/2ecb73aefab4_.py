"""empty message

Revision ID: 2ecb73aefab4
Revises: c0c0a52d94e0
Create Date: 2022-03-04 23:47:24.821310

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2ecb73aefab4"
down_revision = "c0c0a52d94e0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "companies",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column("city", sa.String(length=255), nullable=False),
        sa.Column("state", sa.String(length=255), nullable=False),
        sa.Column("zip", sa.String(length=255), nullable=False),
        sa.Column("registration_number", sa.String(length=255), nullable=False),
        sa.Column("registration_court", sa.String(length=255), nullable=False),
        sa.Column("vat_number", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("companies")
    # ### end Alembic commands ###