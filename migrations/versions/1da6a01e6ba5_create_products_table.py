"""create products table

Revision ID: 1da6a01e6ba5
Revises: ad4e8a36ef64
Create Date: 2024-02-07 11:46:35.537096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '1da6a01e6ba5'
down_revision: Union[str, None] = 'ad4e8a36ef64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('product_name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('product_category', sa.VARCHAR(length=50), nullable=False),
    sa.Column('product_price', sa.FLOAT(), nullable=False),
    sa.Column('stock', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('products')
