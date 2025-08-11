"""create tables

Revision ID: b8383c482697
Revises: 2ee6358fabff
Create Date: 2025-08-11 17:13:03.018308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8383c482697'
down_revision: Union[str, Sequence[str], None] = '2ee6358fabff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
