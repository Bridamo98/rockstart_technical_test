from typing import List

from app.models.models import Instructors
from app.modules.factory import factory_for
from app.modules.schemas import InstructorCreate, InstructorOut, InstructorUpdate
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/instructors",
    tags=["instructors"],
)

INSTRUCTOR_NOT_FOUND_MSG = "Instructor not found"


@router.post("/", response_model=InstructorOut)
def create_instructor(payload: InstructorCreate):
    with factory_for(Instructors) as f:
        inst = Instructors.create(
            name=payload.name, email=payload.email, bio=payload.bio
        )
        obj = f.create(obj=inst, refresh=True)
        return f.serialize(obj)


@router.get("/", response_model=List[InstructorOut])
def list_instructors():
    with factory_for(Instructors) as f:
        objs = f.get_all()
        return f.serialize_many(objs)


@router.get("/{inst_id}", response_model=InstructorOut)
def get_instructor(inst_id: int):
    with factory_for(Instructors) as f:
        obj = f.get_by_id(inst_id)
        if not obj:
            raise HTTPException(status_code=404, detail=INSTRUCTOR_NOT_FOUND_MSG)
        return f.serialize(obj)


@router.put("/{inst_id}", response_model=InstructorOut)
def update_instructor(inst_id: int, payload: InstructorUpdate):
    changes = payload.model_dump(exclude_unset=True)
    with factory_for(Instructors) as f:
        obj = f.update_by_id(inst_id, refresh=True, **changes)
        if not obj:
            raise HTTPException(status_code=404, detail=INSTRUCTOR_NOT_FOUND_MSG)
        return f.serialize(obj)


@router.delete("/{inst_id}")
def delete_instructor(inst_id: int):
    with factory_for(Instructors) as f:
        success = f.delete(inst_id)
        if not success:
            raise HTTPException(status_code=404, detail=INSTRUCTOR_NOT_FOUND_MSG)
        return {"deleted": inst_id}
