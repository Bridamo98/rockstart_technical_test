from typing import List

from app.models.models import Lessons
from app.modules.factory import factory_for
from app.modules.schemas import LessonCreate, LessonOut, LessonUpdate
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/courses/{course_id}/lessons",
    tags=["lessons"],
)

LESSON_NOT_FOUND_MSG = "Lesson not found"


@router.post("/", response_model=LessonOut)
def create_lesson(course_id: int, payload: LessonCreate):
    with factory_for(Lessons) as f:
        inst = Lessons.create(
            course_id=course_id, title=payload.title, video_url=str(payload.video_url)
        )
        obj = f.create(obj=inst, refresh=True)
        return f.serialize(obj)


@router.get("/", response_model=List[LessonOut])
def list_lessons(course_id: int):
    with factory_for(Lessons) as f:
        objs = f.filter(course_id=course_id)
        return f.serialize_many(objs)


@router.get("/{lesson_id}", response_model=LessonOut)
def get_lesson(course_id: int, lesson_id: int):
    with factory_for(Lessons) as f:
        obj = f.get_by_id(lesson_id)
        if not obj or obj.course_id != course_id:
            raise HTTPException(status_code=404, detail=LESSON_NOT_FOUND_MSG)
        return f.serialize(obj)


@router.put("/{lesson_id}", response_model=LessonOut)
def update_lesson(course_id: int, lesson_id: int, payload: LessonUpdate):
    changes = payload.model_dump(exclude_unset=True)
    with factory_for(Lessons) as f:
        obj = f.get_by_id(lesson_id)
        if not obj or obj.course_id != course_id:
            raise HTTPException(status_code=404, detail=LESSON_NOT_FOUND_MSG)
        updated = f.update_by_id(lesson_id, refresh=True, **changes)
        if not updated:
            raise HTTPException(status_code=404, detail=LESSON_NOT_FOUND_MSG)
        return f.serialize(updated)


@router.delete("/{lesson_id}")
def delete_lesson(course_id: int, lesson_id: int):
    with factory_for(Lessons) as f:
        obj = f.get_by_id(lesson_id)
        if not obj or obj.course_id != course_id:
            raise HTTPException(status_code=404, detail=LESSON_NOT_FOUND_MSG)
        f.delete(lesson_id)
        return {"deleted": lesson_id}
