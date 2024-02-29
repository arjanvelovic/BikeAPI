"""empty message

Revision ID: 07e00bcbf2a0
Revises: 
Create Date: 2024-02-18 13:43:12.330765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07e00bcbf2a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bikeconfig',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('make', sa.String(length=20), nullable=False),
    sa.Column('model', sa.String(length=20), nullable=False),
    sa.Column('year', sa.String(length=5), nullable=False),
    sa.Column('color', sa.String(length=30), nullable=False),
    sa.Column('trim', sa.String(length=30), nullable=True),
    sa.Column('category', sa.String(length=30), nullable=True),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('isAdmin', sa.Boolean(), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user_cart',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('BikeConfigID', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['BikeConfigID'], ['bikeconfig.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_cart')
    op.drop_table('user')
    op.drop_table('bikeconfig')
    # ### end Alembic commands ###