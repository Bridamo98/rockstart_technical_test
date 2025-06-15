# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_instructor_create_schema_valid instructor_create'] = {
    'bio': 'Bio',
    'email': 'test@example.com',
    'name': 'Test'
}
