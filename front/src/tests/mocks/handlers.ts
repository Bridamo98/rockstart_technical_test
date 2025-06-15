import { http, HttpResponse } from "msw";
import type { Course, Instructor, Lesson } from "../../types";

const courses: Course[] = [];
const lessons: Lesson[] = [];
const instructors: Instructor[] = [
  { id: 1, name: "Inst", email: "i@e.com", bio: "" },
];

let nextCourseId = 1;
let nextLessonId = 1;
export function resetMockState() {
  courses.length = 0;
  lessons.length = 0;
  nextCourseId = 1;
  nextLessonId = 1;
}

const base = "http://localhost:8000";

export const handlers = [
  /* ───────────── COURSES ───────────── */
  // LIST
  http.get(`${base}/courses/`, () => HttpResponse.json(courses)),

  // CREATE
  http.post(`${base}/courses/`, async ({ request }) => {
    const body = (await request.json()) as Omit<Course, "id">;
    const newCourse: Course = Object.assign({ id: nextCourseId++ }, body);
    courses.push(newCourse);
    return HttpResponse.json(newCourse, { status: 201 });
  }),

  // READ
  http.get(`${base}/courses/:id`, ({ params }) => {
    const course = courses.find((c) => c.id === Number(params.id));
    return course
      ? HttpResponse.json(course)
      : new HttpResponse(null, { status: 404 });
  }),

  // UPDATE
  http.put(`${base}/courses/:id`, async ({ params, request }) => {
    const idx = courses.findIndex((c) => c.id === Number(params.id));
    if (idx === -1) return new HttpResponse(null, { status: 404 });

    const patch = (await request.json()) as Partial<Course>;
    courses[idx] = { ...courses[idx], ...patch };
    return HttpResponse.json(courses[idx]);
  }),

  // DELETE
  http.delete(`${base}/courses/:id`, ({ params }) => {
    const idx = courses.findIndex((c) => c.id === Number(params.id));
    if (idx === -1) return new HttpResponse(null, { status: 404 });

    courses.splice(idx, 1);
    return new HttpResponse(null, { status: 204 });
  }),

  /* ───────────── LESSONS ───────────── */
  // LIST
  http.get(`${base}/courses/:courseId/lessons/`, ({ params }) =>
    HttpResponse.json(
      lessons.filter((l) => l.course_id === Number(params.courseId))
    )
  ),

  // CREATE
  http.post(
    `${base}/courses/:courseId/lessons/`,
    async ({ params, request }) => {
      const body = (await request.json()) as Omit<Lesson, "id" | "course_id">;
      const newLesson: Lesson = Object.assign(
        { id: nextLessonId++, course_id: Number(params.courseId) },
        body
      );
      lessons.push(newLesson);
      return HttpResponse.json(newLesson, { status: 201 });
    }
  ),

  // READ
  http.get(`${base}/courses/:courseId/lessons/:lessonId`, ({ params }) => {
    const lesson = lessons.find((l) => l.id === Number(params.lessonId));
    return lesson && lesson.course_id === Number(params.courseId)
      ? HttpResponse.json(lesson)
      : new HttpResponse(null, { status: 404 });
  }),

  // UPDATE
  http.put(
    `${base}/courses/:courseId/lessons/:lessonId`,
    async ({ params, request }) => {
      const idx = lessons.findIndex((l) => l.id === Number(params.lessonId));
      if (idx === -1 || lessons[idx].course_id !== Number(params.courseId))
        return new HttpResponse(null, { status: 404 });

      const patch = (await request.json()) as Partial<Lesson>;
      lessons[idx] = { ...lessons[idx], ...patch };
      return HttpResponse.json(lessons[idx]);
    }
  ),

  // DELETE
  http.delete(`${base}/courses/:courseId/lessons/:lessonId`, ({ params }) => {
    const idx = lessons.findIndex((l) => l.id === Number(params.lessonId));
    if (idx === -1 || lessons[idx].course_id !== Number(params.courseId))
      return new HttpResponse(null, { status: 404 });

    lessons.splice(idx, 1);
    return new HttpResponse(null, { status: 204 });
  }),

  /* ──────────── INSTRUCTORS ─────────── */
  http.get(`${base}/instructors/`, () => HttpResponse.json(instructors)),
];
