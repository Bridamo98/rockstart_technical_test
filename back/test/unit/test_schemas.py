import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

import pytest
from app.modules.schemas import InstructorCreate
from pydantic import ValidationError


def test_instructor_create_schema_valid(snapshot):
    data = {"name": "Test", "email": "test@example.com", "bio": "Bio"}
    inst = InstructorCreate(**data)
    # Guarda snapshot de la representación dict
    snapshot.assert_match(inst.model_dump(), "instructor_create")


@pytest.mark.parametrize("email", ["bademail", "@nope.com"])
def test_instructor_create_schema_invalid_email(email):
    with pytest.raises(ValidationError):
        InstructorCreate(name="A", email=email, bio="B")
