"""empty message

Revision ID: 2d784805e806
Revises: 
Create Date: 2020-06-05 14:36:01.707845

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d784805e806'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('top_image', 'id',
               existing_type=mysql.SMALLINT(display_width=5, unsigned=True),
               comment='顶图id',
               autoincrement=True)
    op.alter_column('top_image', 'url',
               existing_type=mysql.VARCHAR(length=255),
               comment='顶图url',
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('top_image', 'url',
               existing_type=mysql.VARCHAR(length=255),
               comment=None,
               existing_comment='顶图url',
               existing_nullable=True)
    op.alter_column('top_image', 'id',
               existing_type=mysql.SMALLINT(display_width=5, unsigned=True),
               comment=None,
               existing_comment='顶图id',
               autoincrement=True)
    # ### end Alembic commands ###
