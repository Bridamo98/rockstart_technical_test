import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

import pytest
from app.modules.schemas import CourseCreate, CourseUpdate
from pydantic import ValidationError


def test_course_create_schema_valid(snapshot):
    obj = CourseCreate(title="Course", course_desc="Desc", instructor_id=1)
    snapshot.assert_match(obj.model_dump(), "course_create")


def test_course_create_title_max_length():
    with pytest.raises(ValidationError):
        CourseCreate(title="A" * 256, course_desc="d", instructor_id=1)


def test_course_update_empty_exclude_unset():
    upd = CourseUpdate()  # type: ignore
    assert upd.model_dump(exclude_unset=True) == {}


def test_course_update_invalid_title_length():
    with pytest.raises(ValidationError):
        CourseUpdate(title="B" * 256)
