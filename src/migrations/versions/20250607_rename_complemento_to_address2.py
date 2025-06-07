"""Volta o campo complemento para address2 na tabela orders

Revision ID: 20250607_rename_complemento_to_address2
Revises: 20250607_rename_address2_to_complemento
Create Date: 2025-06-07
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20250607_rename_complemento_to_address2'
down_revision = '20250607_rename_address2_to_complemento'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('orders', 'complemento', new_column_name='address2', existing_type=sa.String(length=255), existing_nullable=True)

def downgrade():
    op.alter_column('orders', 'address2', new_column_name='complemento', existing_type=sa.String(length=255), existing_nullable=True)
