"""Add initial inserts

Revision ID: a2ea65c1f5b4
Revises: 398f0537a1bd
Create Date: 2025-06-14 15:22:16.699026

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a2ea65c1f5b4"
down_revision: Union[str, None] = "398f0537a1bd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    for table in ["lessons", "courses", "instructors"]:
        if conn.dialect.has_table(conn, table):
            op.execute(f"DELETE FROM {table}")

    instructors = sa.table(
        "instructors",
        sa.column("name", sa.String),
        sa.column("email", sa.String),
        sa.column("bio", sa.Text),
    )
    courses = sa.table(
        "courses",
        sa.column("title", sa.String),
        sa.column("course_desc", sa.Text),
        sa.column("instructor_id", sa.Integer),
    )
    lessons = sa.table(
        "lessons",
        sa.column("course_id", sa.Integer),
        sa.column("title", sa.String),
        sa.column("video_url", sa.String),
    )

    op.bulk_insert(
        instructors,
        [
            {
                "name": "Ana Martínez",
                "email": "ana.martinez@example.com",
                "bio": "Especialista en matemáticas aplicadas y educación online.",
            },
            {
                "name": "Carlos Gómez",
                "email": "carlos.gomez@example.com",
                "bio": "Ingeniero de software con experiencia en desarrollo web y móvil.",
            },
            {
                "name": "Lucía Fernández",
                "email": "lucia.fernandez@example.com",
                "bio": "Doctora en física y apasionada por la enseñanza.",
            },
            {
                "name": "Pedro Ramírez",
                "email": "pedro.ramirez@example.com",
                "bio": "Experto en inteligencia artificial y machine learning.",
            },
            {
                "name": "María López",
                "email": "maria.lopez@example.com",
                "bio": "Profesora de química con más de 10 años de experiencia.",
            },
            {
                "name": "Javier Torres",
                "email": "javier.torres@example.com",
                "bio": "Desarrollador backend y entusiasta de bases de datos.",
            },
        ],
    )

    op.bulk_insert(
        courses,
        [
            {
                "title": "Matemáticas Básicas",
                "course_desc": "Curso introductorio a las matemáticas básicas.",
                "instructor_id": 1,
            },
            {
                "title": "Desarrollo Web",
                "course_desc": "Aprende a crear sitios web modernos.",
                "instructor_id": 2,
            },
            {
                "title": "Física Avanzada",
                "course_desc": "Explora conceptos avanzados de física.",
                "instructor_id": 3,
            },
            {
                "title": "Inteligencia Artificial",
                "course_desc": "Introducción a los conceptos y aplicaciones de IA.",
                "instructor_id": 4,
            },
            {
                "title": "Química General",
                "course_desc": "Fundamentos de la química para principiantes.",
                "instructor_id": 5,
            },
            {
                "title": "Bases de Datos",
                "course_desc": "Aprende sobre diseño y gestión de bases de datos.",
                "instructor_id": 6,
            },
            {
                "title": "Machine Learning",
                "course_desc": "Curso práctico de aprendizaje automático.",
                "instructor_id": 4,
            },
            {
                "title": "Química Orgánica",
                "course_desc": "Estudio de compuestos orgánicos y sus reacciones.",
                "instructor_id": 5,
            },
        ],
    )

    op.bulk_insert(
        lessons,
        [
            {
                "course_id": 1,
                "title": "Introducción a las Matemáticas",
                "video_url": "https://www.youtube.com/watch?v=-RDBMu7BreE&pp=ygUaaW50cm9kdWNjaW9uIGEgbWF0ZW1hdGljYXM%3D",
            },
            {
                "course_id": 1,
                "title": "Álgebra Básica",
                "video_url": "https://www.youtube.com/watch?v=_6uyQISZvBc&pp=ygUOYWxnZWJyYSBiYXNpY2E%3D",
            },
            {
                "course_id": 2,
                "title": "HTML y CSS",
                "video_url": "https://www.youtube.com/watch?v=ELSm-G201Ls&pp=ygUKaHRtbCB5IGNzcw%3D%3D",
            },
            {
                "course_id": 2,
                "title": "JavaScript Básico",
                "video_url": "https://www.youtube.com/watch?v=QoC4RxNIs5M&pp=ygUSSmF2YVNjcmlwdCBCw6FzaWNv",
            },
            {
                "course_id": 3,
                "title": "Mecánica Clásica",
                "video_url": "https://www.youtube.com/watch?v=psms00DeX9o&pp=ygUYbWVjw6FuaWNhIGNsw6FzaWNhIGN1cnNv",
            },
            {
                "course_id": 3,
                "title": "Electromagnetismo",
                "video_url": "https://www.youtube.com/watch?v=cFaf1_P2Y8c&pp=ygUXRWxlY3Ryb21hZ25ldGlzbW8gY3Vyc28%3D",
            },
            {
                "course_id": 4,
                "title": "Introducción a la IA",
                "video_url": "https://www.youtube.com/watch?v=CjdusCm73p0&pp=ygUVSW50cm9kdWNjacOzbiBhIGxhIElB",
            },
            {
                "course_id": 4,
                "title": "Redes Neuronales",
                "video_url": "https://www.youtube.com/watch?v=jKCQsndqEGQ&pp=ygUWUmVkZXMgTmV1cm9uYWxlcyBjdXJzbw%3D%3D",
            },
            {
                "course_id": 5,
                "title": "Estructura Atómica",
                "video_url": "https://www.youtube.com/watch?v=Xvno5NeanxU&pp=ygUZRXN0cnVjdHVyYSBBdMOzbWljYSBjdXJzbw%3D%3D",
            },
            {
                "course_id": 5,
                "title": "Reacciones Químicas",
                "video_url": "https://www.youtube.com/watch?v=smlrUR_UXnk&pp=ygUaUmVhY2Npb25lcyBRdcOtbWljYXMgY3Vyc28%3D",
            },
            {
                "course_id": 6,
                "title": "Modelado de Datos",
                "video_url": "https://www.youtube.com/watch?v=aFgHVE_Y_YU&pp=ygUXTW9kZWxhZG8gZGUgRGF0b3MgY3Vyc28%3D",
            },
            {
                "course_id": 6,
                "title": "SQL Básico",
                "video_url": "https://www.youtube.com/watch?v=OuJerKzV5T0&pp=ygURU1FMIELDoXNpY28gY3Vyc2_SBwkJ3gkBhyohjO8%3D",
            },
            {
                "course_id": 7,
                "title": "Regresión Lineal",
                "video_url": "https://www.youtube.com/watch?v=k964_uNn3l0&t=141s&pp=ygUaUmVncmVzacOzbiBMaW5lYWwgY3Vyc28gSUHSBwkJ3gkBhyohjO8%3D",
            },
            {
                "course_id": 7,
                "title": "Clasificación",
                "video_url": "https://www.youtube.com/watch?v=8-nt3Urok4E&pp=ygUkQ2xhc2lmaWNhY2NvbiBtYWNoaW5sZSBjdXJzbw%3D%3D",
            },
            {
                "course_id": 8,
                "title": "Hidrocarburos",
                "video_url": "https://www.youtube.com/watch?v=itVIgu2WAU8&pp=ygUTSGlkcm9jYXJidXJvcyBjdXJzbw%3D%3Ds",
            },
            {
                "course_id": 8,
                "title": "Reacciones Orgánicas",
                "video_url": "https://www.youtube.com/watch?v=gdHecHHkj38&pp=ygUbUmVhY2Npb25lcyBPcmfDoW5pY2FzIGN1cnNv",
            },
        ],
    )


def downgrade() -> None:
    conn = op.get_bind()
    for table in ["lessons", "courses", "instructors"]:
        if conn.dialect.has_table(conn, table):
            op.execute(f"DELETE FROM {table}")
