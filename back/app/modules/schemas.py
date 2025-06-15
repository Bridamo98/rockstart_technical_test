from typing import Optional

from pydantic import BaseModel, EmailStr, Field, HttpUrl, field_validator, validator


# Instructor schemas
class InstructorCreate(BaseModel):
    name: str = Field(..., max_length=255)
    email: EmailStr = Field(..., max_length=255)
    bio: str


class InstructorUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = Field(None, max_length=255)
    bio: Optional[str] = None


class InstructorOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    bio: str


# Course schemas
class CourseCreate(BaseModel):
    title: str = Field(..., max_length=255)
    course_desc: str
    instructor_id: int


class CourseUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    course_desc: Optional[str] = None


class CourseOut(BaseModel):
    id: int
    title: str
    course_desc: str
    instructor_id: int


# Lesson schemas
class LessonCreate(BaseModel):
    title: str = Field(..., max_length=255)
    video_url: HttpUrl

    @validator("video_url")
    def must_be_youtube(cls, v: HttpUrl) -> HttpUrl:
        url_str = str(v)
        if not ("youtube.com/watch?v=" in url_str or "youtu.be/" in url_str):
            raise ValueError("video_url must be a YouTube link")
        return v


class LessonUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    video_url: Optional[HttpUrl] = None

    @field_validator("video_url")
    def must_be_youtube(cls, v: Optional[HttpUrl]) -> Optional[HttpUrl]:
        if v is None:
            return v
        url_str = str(v)
        if not ("youtube.com/watch?v=" in url_str or "youtu.be/" in url_str):
            raise ValueError("video_url must be a YouTube link")
        return v


class LessonOut(BaseModel):
    id: int
    course_id: int
    title: str
    video_url: HttpUrl
