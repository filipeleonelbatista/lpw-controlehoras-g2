"""empty message

Revision ID: 05dd8bcc361e
Revises: dcc82f04066a
Create Date: 2018-05-27 18:47:30.967282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05dd8bcc361e'
down_revision = 'dcc82f04066a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_client_nameEmpresa', table_name='client')
    op.create_index(op.f('ix_client_nameEmpresa'), 'client', ['nameEmpresa'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_client_nameEmpresa'), table_name='client')
    op.create_index('ix_client_nameEmpresa', 'client', ['nameEmpresa'], unique=1)
    # ### end Alembic commands ###