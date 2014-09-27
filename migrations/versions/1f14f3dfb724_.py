"""empty message

Revision ID: 1f14f3dfb724
Revises: None
Create Date: 2014-09-27 22:17:10.747910

"""

# revision identifiers, used by Alembic.
revision = '1f14f3dfb724'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('background',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_back', sa.Integer(), nullable=True),
    sa.Column('image_key', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_back'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('background')
    ### end Alembic commands ###
