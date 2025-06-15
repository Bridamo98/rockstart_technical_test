import type { Lesson, LessonCreateDTO, LessonUpdateDTO } from "../types";
import { api } from "./client";

export const LessonsAPI = {
  list: (courseId: number) =>
    api.get<Lesson[]>(`/courses/${courseId}/lessons/`),
  get: (courseId: number, id: number) =>
    api.get<Lesson>(`/courses/${courseId}/lessons/${id}`),
  create: (courseId: number, payload: LessonCreateDTO) =>
    api.post<Lesson>(`/courses/${courseId}/lessons/`, payload),
  update: (courseId: number, id: number, payload: LessonUpdateDTO) =>
    api.put<Lesson>(`/courses/${courseId}/lessons/${id}`, payload),
  remove: (courseId: number, id: number) =>
    api.delete(`/courses/${courseId}/lessons/${id}`),
};
