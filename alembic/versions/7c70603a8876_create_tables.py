"""create tables

Revision ID: 7c70603a8876
Revises: b8383c482697
Create Date: 2025-08-11 17:17:47.699248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c70603a8876'
down_revision: Union[str, Sequence[str], None] = 'b8383c482697'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
