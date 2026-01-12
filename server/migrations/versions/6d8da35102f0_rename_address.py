"""rename address

Revision ID: 6d8da35102f0
Revises: 458ea643186e
Create Date: 2026-01-12 12:02:37.220559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d8da35102f0'
down_revision = '458ea643186e'
branch_labels = None
depends_on = None

def upgrade():
    # rename column 'address' → 'location'
    op.alter_column('departments', 'address', new_column_name='location')


def downgrade():
    # rename column back 'location' → 'address'
    op.alter_column('departments', 'location', new_column_name='address')
