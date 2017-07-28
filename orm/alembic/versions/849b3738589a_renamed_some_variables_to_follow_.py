"""renamed some variables to follow convention

Revision ID: 849b3738589a
Revises: 94ba0817bee4
Create Date: 2017-07-21 16:56:44.462013

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '849b3738589a'
down_revision = '94ba0817bee4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('is_deleted', sa.BOOLEAN(), nullable=False))
    op.drop_column('game', 'isDeleted')
    op.add_column('user', sa.Column('is_deleted', sa.BOOLEAN(), nullable=False))
    op.drop_column('user', 'isDeleted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('isDeleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('user', 'is_deleted')
    op.add_column('game', sa.Column('isDeleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('game', 'is_deleted')
    # ### end Alembic commands ###
