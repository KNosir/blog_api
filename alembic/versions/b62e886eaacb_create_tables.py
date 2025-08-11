"""create tables

Revision ID: b62e886eaacb
Revises: 7c70603a8876
Create Date: 2025-08-11 17:22:11.013677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b62e886eaacb'
down_revision: Union[str, Sequence[str], None] = '7c70603a8876'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
