"""empty message

Revision ID: 5f2965ee8957
Revises: 80db32e2657c
Create Date: 2022-03-03 15:41:04.764402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f2965ee8957'
down_revision = '80db32e2657c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('price', sa.REAL(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='items_pkey'),
    sa.UniqueConstraint('name', name='items_name_key')
    )
    # ### end Alembic commands ###
