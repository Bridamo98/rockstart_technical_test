# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_crud_course_flow api_create_course'] = {
    'course_desc': 'Course description',
    'id': 9,
    'instructor_id': 7,
    'title': 'Intro to Testing'
}

snapshots['test_crud_course_flow api_list_courses'] = [
    {
        'course_desc': 'Curso introductorio a las matemáticas básicas.',
        'id': 1,
        'instructor_id': 1,
        'title': 'Matemáticas Básicas'
    },
    {
        'course_desc': 'Aprende a crear sitios web modernos.',
        'id': 2,
        'instructor_id': 2,
        'title': 'Desarrollo Web'
    },
    {
        'course_desc': 'Explora conceptos avanzados de física.',
        'id': 3,
        'instructor_id': 3,
        'title': 'Física Avanzada'
    },
    {
        'course_desc': 'Introducción a los conceptos y aplicaciones de IA.',
        'id': 4,
        'instructor_id': 4,
        'title': 'Inteligencia Artificial'
    },
    {
        'course_desc': 'Fundamentos de la química para principiantes.',
        'id': 5,
        'instructor_id': 5,
        'title': 'Química General'
    },
    {
        'course_desc': 'Aprende sobre diseño y gestión de bases de datos.',
        'id': 6,
        'instructor_id': 6,
        'title': 'Bases de Datos'
    },
    {
        'course_desc': 'Curso práctico de aprendizaje automático.',
        'id': 7,
        'instructor_id': 4,
        'title': 'Machine Learning'
    },
    {
        'course_desc': 'Estudio de compuestos orgánicos y sus reacciones.',
        'id': 8,
        'instructor_id': 5,
        'title': 'Química Orgánica'
    },
    {
        'course_desc': 'Course description',
        'id': 9,
        'instructor_id': 7,
        'title': 'Intro to Testing'
    }
]

snapshots['test_crud_course_flow api_update_course'] = {
    'course_desc': 'Course description',
    'id': 9,
    'instructor_id': 7,
    'title': 'Intro to Testing – updated'
}
