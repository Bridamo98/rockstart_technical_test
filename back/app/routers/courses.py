from typing import List

from app.models.models import Courses
from app.modules.factory import factory_for
from app.modules.schemas import CourseCreate, CourseOut, CourseUpdate
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)

COURSE_NOT_FOUND_MSG = "Course not found"


@router.post("/", response_model=CourseOut)
def create_course(payload: CourseCreate):
    with factory_for(Courses) as f:
        inst = Courses.create(
            title=payload.title,
            course_desc=payload.course_desc,
            instructor_id=payload.instructor_id,
        )
        obj = f.create(obj=inst, refresh=True)
        return f.serialize(obj)


@router.get("/", response_model=List[CourseOut])
def list_courses():
    with factory_for(Courses) as f:
        objs = f.get_all()
        return f.serialize_many(objs)


@router.get("/{course_id}", response_model=CourseOut)
def get_course(course_id: int):
    with factory_for(Courses) as f:
        obj = f.get_by_id(course_id)
        if not obj:
            raise HTTPException(status_code=404, detail=COURSE_NOT_FOUND_MSG)
        return f.serialize(obj)


@router.put("/{course_id}", response_model=CourseOut)
def update_course(course_id: int, payload: CourseUpdate):
    changes = payload.model_dump(exclude_unset=True)
    with factory_for(Courses) as f:
        obj = f.update_by_id(course_id, refresh=True, **changes)
        if not obj:
            raise HTTPException(status_code=404, detail=COURSE_NOT_FOUND_MSG)
        return f.serialize(obj)


@router.delete("/{course_id}")
def delete_course(course_id: int):
    with factory_for(Courses) as f:
        success = f.delete(course_id)
        if not success:
            raise HTTPException(status_code=404, detail=COURSE_NOT_FOUND_MSG)
        return {"deleted": course_id}
