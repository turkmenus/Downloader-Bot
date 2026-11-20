"""Add language column to settings table.

Revision ID: 20261120_000014
Revises: 20260914_000013
Create Date: 2026-11-20 14:25:00.000000
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "20261120_000014"
down_revision: Union[str, Sequence[str], None] = "20260914_000013"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    columns = {col["name"] for col in inspector.get_columns("settings")}
    if "language" not in columns:
        op.add_column(
            "settings",
            sa.Column(
                "language",
                sa.Text(),
                server_default=sa.text("'tr'"),
                nullable=False,
            ),
        )


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    columns = {col["name"] for col in inspector.get_columns("settings")}
    if "language" in columns:
        op.drop_column("settings", "language")
