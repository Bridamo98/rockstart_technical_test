export interface Instructor {
  id: number;
  name: string;
  email: string;
  bio: string;
}

export interface Course {
  id: number;
  title: string;
  course_desc: string;
  instructor_id: number;
}

export interface Lesson {
  id: number;
  course_id: number;
  title: string;
  video_url: string;
}

export type CourseCreateDTO = Omit<Course, "id">;
export type CourseUpdateDTO = Partial<CourseCreateDTO>;

export type LessonCreateDTO = Omit<Lesson, "id" | "course_id">;
export type LessonUpdateDTO = Partial<LessonCreateDTO>;
