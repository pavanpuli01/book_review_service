"""Add index to reviews.book_id

Revision ID: d12f4a3a3b74
Revises: 9d3b318410e0
Create Date: 2025-06-29 01:44:17.647979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd12f4a3a3b74'
down_revision: Union[str, Sequence[str], None] = '9d3b318410e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
