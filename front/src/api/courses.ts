import type { Course, CourseCreateDTO, CourseUpdateDTO } from "../types";
import { api } from "./client";

export const CoursesAPI = {
  list: () => api.get<Course[]>("/courses/"),
  get: (id: number) => api.get<Course>(`/courses/${id}`),
  create: (payload: CourseCreateDTO) => api.post<Course>("/courses/", payload),
  update: (id: number, payload: CourseUpdateDTO) =>
    api.put<Course>(`/courses/${id}`, payload),
  remove: (id: number) => api.delete(`/courses/${id}`),
};
