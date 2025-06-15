# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_course_create_schema_valid course_create'] = {
    'course_desc': 'Desc',
    'instructor_id': 1,
    'title': 'Course'
}
