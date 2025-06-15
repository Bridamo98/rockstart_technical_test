"""Create initial tables

Revision ID: 398f0537a1bd
Revises:
Create Date: 2025-06-14 15:09:16.711804

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "398f0537a1bd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    for table in ["lessons", "courses", "instructors"]:
        if conn.dialect.has_table(conn, table):
            op.drop_table(table)

    op.create_table(
        "instructors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("bio", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id", name="instructors_pkey"),
    )
    op.create_table(
        "courses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("course_desc", sa.Text(), nullable=False),
        sa.Column("instructor_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["instructor_id"],
            ["instructors.id"],
            name="fk_courses_instructor_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="courses_pkey"),
    )
    op.create_table(
        "lessons",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("course_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("video_url", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["courses.id"],
            name="fk_lessons_course_id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="lessons_pkey"),
    )


def downgrade() -> None:
    conn = op.get_bind()
    for table in ["lessons", "courses", "instructors"]:
        if conn.dialect.has_table(conn, table):
            op.execute(f"DELETE FROM {table}")
