"""create tables

Revision ID: 2ee6358fabff
Revises: a0ae3b86ff6e
Create Date: 2025-08-11 17:10:53.458622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ee6358fabff'
down_revision: Union[str, Sequence[str], None] = 'a0ae3b86ff6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
