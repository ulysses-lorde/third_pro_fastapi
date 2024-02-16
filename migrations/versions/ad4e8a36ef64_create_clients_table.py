"""create clients table

Revision ID: ad4e8a36ef64
Revises: 
Create Date: 2024-02-07 11:43:46.214364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'ad4e8a36ef64'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('clients',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('cpf', sa.CHAR(length=14), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('clients')
