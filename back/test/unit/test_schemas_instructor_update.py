import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)


import pytest
from app.modules.schemas import InstructorUpdate
from pydantic import ValidationError


def test_instructor_update_empty():
    upd = InstructorUpdate()  # type: ignore
    assert upd.model_dump(exclude_unset=True) == {}


def test_instructor_update_invalid_email():
    with pytest.raises(ValidationError):
        InstructorUpdate(email="not-an-email")  # type: ignore
