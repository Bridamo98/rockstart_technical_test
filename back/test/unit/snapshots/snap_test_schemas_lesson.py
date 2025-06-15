# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_lesson_create_valid lesson_create'] = {
    'title': 'Lesson',
    'video_url': GenericRepr("HttpUrl('https://www.youtube.com/watch?v=dQw4w9WgXcQ')")
}

snapshots['test_lesson_update_partial lesson_update_partial'] = {
    'title': 'Only title'
}
