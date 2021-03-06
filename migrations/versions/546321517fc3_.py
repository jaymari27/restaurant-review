"""empty message

Revision ID: 546321517fc3
Revises: 
Create Date: 2021-09-14 09:15:35.847679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '546321517fc3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_ratinglist')
    op.alter_column('tbl_admin', 'username',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)
    op.alter_column('tbl_admin', 'password',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tbl_admin', 'password',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('tbl_admin', 'username',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)
    op.create_table('tbl_ratinglist',
    sa.Column('ratingid', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('rating', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('ratingid', name='tbl_ratinglist_pkey')
    )
    # ### end Alembic commands ###
