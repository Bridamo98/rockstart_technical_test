import * as z from "zod";
import { isYoutubeUrl } from "../utils/youtube";

export const courseSchema = z.object({
  title: z
    .string()
    .min(1, "Title is required")
    .max(255, "Title must be ≤ 255 chars"),
  course_desc: z.string().min(1, "Description is required"),
  instructor_id: z.number().int(),
});
export type CourseFormData = z.infer<typeof courseSchema>;

export const lessonSchema = z.object({
  title: z
    .string()
    .min(1, "Title is required")
    .max(255, "Title must be ≤ 255 chars"),
  video_url: z
    .string()
    .url("Invalid URL")
    .refine(isYoutubeUrl, { message: "Must be a YouTube link" }),
});
export type LessonFormData = z.infer<typeof lessonSchema>;
