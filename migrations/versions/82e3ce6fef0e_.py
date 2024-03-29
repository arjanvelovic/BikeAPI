"""empty message

Revision ID: 82e3ce6fef0e
Revises: 0e6b1bdc9a56
Create Date: 2024-02-28 21:59:41.244494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82e3ce6fef0e'
down_revision = '0e6b1bdc9a56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'usercc', ['cc_num'])
    op.add_column('userpayment', sa.Column('delivery_details', sa.PickleType(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userpayment', 'delivery_details')
    op.drop_constraint(None, 'usercc', type_='unique')
    # ### end Alembic commands ###
