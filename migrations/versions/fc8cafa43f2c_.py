"""empty message

Revision ID: fc8cafa43f2c
Revises: 0019b511adc0
Create Date: 2018-07-16 00:02:46.484067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8cafa43f2c'
down_revision = '0019b511adc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('commenter_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['commenter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'posted')
    op.drop_column('comments', 'commenter_id')
    op.drop_table('users')
    # ### end Alembic commands ###
