# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_crud_lesson_flow api_create_lesson'] = {
    'course_id': 10,
    'id': 17,
    'title': 'Lesson 1',
    'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
}

snapshots['test_crud_lesson_flow api_list_lessons'] = [
    {
        'course_id': 10,
        'id': 17,
        'title': 'Lesson 1',
        'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    }
]

snapshots['test_crud_lesson_flow api_update_lesson'] = {
    'course_id': 10,
    'id': 17,
    'title': 'Lesson 1 updated',
    'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
}
