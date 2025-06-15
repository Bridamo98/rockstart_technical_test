from typing import List

from sqlalchemy import ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Instructors(Base):
    __tablename__ = "instructors"

    def __init__(self):
        # Intentional empty constructor due this code is generated automatically
        pass

    __table_args__ = (PrimaryKeyConstraint("id", name="instructors_pkey"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    bio: Mapped[str] = mapped_column(Text)

    @classmethod
    def create(cls, name: str, email: str, bio: str):
        obj = cls()
        obj.name = name
        obj.email = email
        obj.bio = bio
        return obj

    courses: Mapped[List["Courses"]] = relationship(
        "Courses", back_populates="instructor", cascade="all, delete-orphan"
    )


class Courses(Base):
    __tablename__ = "courses"

    def __init__(self):
        # Intentional empty constructor due this code is generated automatically
        pass

    __table_args__ = (
        ForeignKeyConstraint(
            ["instructor_id"],
            ["instructors.id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="fk_courses_instructor_id",
        ),
        PrimaryKeyConstraint("id", name="courses_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    course_desc: Mapped[str] = mapped_column(Text)
    instructor_id: Mapped[int] = mapped_column(Integer)

    @classmethod
    def create(cls, title: str, course_desc: str, instructor_id: int):
        obj = cls()
        obj.title = title
        obj.course_desc = course_desc
        obj.instructor_id = instructor_id
        return obj

    instructor: Mapped["Instructors"] = relationship(
        "Instructors", back_populates="courses"
    )
    lessons: Mapped[List["Lessons"]] = relationship(
        "Lessons", back_populates="course", cascade="all, delete-orphan"
    )


class Lessons(Base):
    __tablename__ = "lessons"

    def __init__(self):
        # Intentional empty constructor due this code is generated automatically
        pass

    __table_args__ = (
        ForeignKeyConstraint(
            ["course_id"],
            ["courses.id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="fk_lessons_course_id",
        ),
        PrimaryKeyConstraint("id", name="lessons_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(255))
    video_url: Mapped[str] = mapped_column(Text)

    @classmethod
    def create(cls, course_id: int, title: str, video_url: str):
        obj = cls()
        obj.course_id = course_id
        obj.title = title
        obj.video_url = video_url
        return obj

    course: Mapped["Courses"] = relationship("Courses", back_populates="lessons")
