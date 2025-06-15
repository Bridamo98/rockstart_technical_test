import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)


import pytest
from app.modules.schemas import LessonCreate, LessonUpdate
from pydantic import ValidationError


def test_lesson_create_valid(snapshot):
    obj = LessonCreate(
        title="Lesson",
        video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # type: ignore
    )
    snapshot.assert_match(obj.model_dump(), "lesson_create")


@pytest.mark.parametrize(
    "url",
    [
        "https://vimeo.com/123",
        "http://example.com/video",
        "https://www.youtube.com/playlist?list=abc",
    ],
)
def test_lesson_create_invalid_url(url):
    with pytest.raises(ValidationError):
        LessonCreate(title="Bad", video_url=url)


def test_lesson_update_partial(snapshot):
    upd = LessonUpdate(title="Only title")
    snapshot.assert_match(upd.model_dump(exclude_unset=True), "lesson_update_partial")
