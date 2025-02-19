"""create todos table

Revision ID: 4248c871351e
Revises: 
Create Date: 2025-02-14 18:14:12.617616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4248c871351e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)

def downgrade():
    op.execute("drop table todos;")
