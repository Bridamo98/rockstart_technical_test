# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_and_get_instructor api_create_instructor'] = {
    'bio': 'Instructor',
    'email': 'alice@example.com',
    'id': 8,
    'name': 'Alice'
}

snapshots['test_create_and_get_instructor api_list_instructors'] = [
    {
        'bio': 'Especialista en matemáticas aplicadas y educación online.',
        'email': 'ana.martinez@example.com',
        'id': 1,
        'name': 'Ana Martínez'
    },
    {
        'bio': 'Ingeniero de software con experiencia en desarrollo web y móvil.',
        'email': 'carlos.gomez@example.com',
        'id': 2,
        'name': 'Carlos Gómez'
    },
    {
        'bio': 'Doctora en física y apasionada por la enseñanza.',
        'email': 'lucia.fernandez@example.com',
        'id': 3,
        'name': 'Lucía Fernández'
    },
    {
        'bio': 'Experto en inteligencia artificial y machine learning.',
        'email': 'pedro.ramirez@example.com',
        'id': 4,
        'name': 'Pedro Ramírez'
    },
    {
        'bio': 'Profesora de química con más de 10 años de experiencia.',
        'email': 'maria.lopez@example.com',
        'id': 5,
        'name': 'María López'
    },
    {
        'bio': 'Desarrollador backend y entusiasta de bases de datos.',
        'email': 'javier.torres@example.com',
        'id': 6,
        'name': 'Javier Torres'
    },
    {
        'bio': 'Instructor',
        'email': 'alice@example.com',
        'id': 8,
        'name': 'Alice'
    }
]
