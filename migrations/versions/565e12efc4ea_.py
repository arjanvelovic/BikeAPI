"""empty message

Revision ID: 565e12efc4ea
Revises: 82e3ce6fef0e
Create Date: 2024-03-07 21:57:32.883277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565e12efc4ea'
down_revision = '82e3ce6fef0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usercc')
    with op.batch_alter_table('bikeconfig', schema=None) as batch_op:
        batch_op.alter_column('cost',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=False)

    with op.batch_alter_table('usercart', schema=None) as batch_op:
        batch_op.alter_column('itemtotal',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Numeric(precision=20, scale=2),
               existing_nullable=True)

    with op.batch_alter_table('userpayment', schema=None) as batch_op:
        batch_op.alter_column('subtotal',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Numeric(precision=20, scale=2),
               existing_nullable=False)
        batch_op.alter_column('tax',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Numeric(precision=20, scale=2),
               existing_nullable=False)
        batch_op.alter_column('total',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Numeric(precision=20, scale=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userpayment', schema=None) as batch_op:
        batch_op.alter_column('total',
               existing_type=sa.Numeric(precision=20, scale=2),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=False)
        batch_op.alter_column('tax',
               existing_type=sa.Numeric(precision=20, scale=2),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=False)
        batch_op.alter_column('subtotal',
               existing_type=sa.Numeric(precision=20, scale=2),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=False)

    with op.batch_alter_table('usercart', schema=None) as batch_op:
        batch_op.alter_column('itemtotal',
               existing_type=sa.Numeric(precision=20, scale=2),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=True)

    with op.batch_alter_table('bikeconfig', schema=None) as batch_op:
        batch_op.alter_column('cost',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.INTEGER(),
               existing_nullable=False)

    op.create_table('usercc',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('user_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('cc_num', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('cc_date', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('cc_code', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.Column('cc_zip', sa.VARCHAR(length=9), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], name='usercc_user_token_fkey'),
    sa.PrimaryKeyConstraint('id', name='usercc_pkey'),
    sa.UniqueConstraint('cc_num', name='usercc_cc_num_key')
    )
    # ### end Alembic commands ###