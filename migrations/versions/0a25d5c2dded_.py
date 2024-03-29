"""empty message

Revision ID: 0a25d5c2dded
Revises: c9a5faaf6a28
Create Date: 2024-02-19 08:20:16.691156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a25d5c2dded'
down_revision = 'c9a5faaf6a28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usercc',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.Column('cc_num', sa.String(length=20), nullable=False),
    sa.Column('cc_date', sa.String(length=10), nullable=False),
    sa.Column('cc_code', sa.String(length=5), nullable=False),
    sa.Column('cc_zip', sa.String(length=9), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userpayment',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.Column('items', sa.PickleType(), nullable=False),
    sa.Column('subtotal', sa.String(length=10), nullable=False),
    sa.Column('tax', sa.String(length=5), nullable=False),
    sa.Column('total', sa.String(length=9), nullable=False),
    sa.Column('date_placed', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('address_street', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('address_city', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('address_state', sa.String(length=2), nullable=True))
    op.add_column('user', sa.Column('address_zipcode', sa.String(length=9), nullable=True))
    op.drop_column('user', 'address')
    op.add_column('usercart', sa.Column('subtotal', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usercart', 'subtotal')
    op.add_column('user', sa.Column('address', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('user', 'address_zipcode')
    op.drop_column('user', 'address_state')
    op.drop_column('user', 'address_city')
    op.drop_column('user', 'address_street')
    op.drop_table('userpayment')
    op.drop_table('usercc')
    # ### end Alembic commands ###
