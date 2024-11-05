"""otros modelos

Revision ID: fffffdaa4b51
Revises: 3eb536d940cc
Create Date: 2024-11-05 19:08:25.983471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fffffdaa4b51'
down_revision = '3eb536d940cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('modelo', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('celular',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modelo', sa.String(length=50), nullable=False),
    sa.Column('anio_fabricacion', sa.Integer(), nullable=True),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('celular')
    op.drop_table('marca')
    # ### end Alembic commands ###
