"""empty message

Revision ID: 6b911f42c563
Revises: 
Create Date: 2024-11-13 18:23:12.967299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b911f42c563'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('specialists')
    op.drop_table('services')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('services_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('duration', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='services_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('specialists',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('specialists_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='specialists_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('service_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('specialist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], name='orders_service_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['specialist_id'], ['specialists.id'], name='orders_specialist_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='orders_pkey')
    )
    # ### end Alembic commands ###
