import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import * as z from "zod";

import { extractYoutubeId } from "../utils/youtube";

const isYoutubeUrl = (url: string) => !!extractYoutubeId(url);

const createSchema = z.object({
  title: z
    .string()
    .min(1, "Title is required")
    .max(255, "Title must be ≤ 255 characters"),
  video_url: z
    .string()
    .url("Invalid URL")
    .refine(isYoutubeUrl, { message: "Must be a YouTube link" }),
});
const updateSchema = createSchema.partial();

type CreateFormData = z.infer<typeof createSchema>;
type UpdateFormData = z.infer<typeof updateSchema>;
type FormData = CreateFormData | UpdateFormData;

interface Props {
  defaultValues?: UpdateFormData;
  onSubmit: (values: FormData) => void | Promise<void>;
  submitLabel?: string;
}

export default function LessonForm({
  defaultValues,
  onSubmit,
  submitLabel = "Save",
}: Props) {
  const isEdit = !!defaultValues;
  const schema = isEdit ? updateSchema : createSchema;

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>({
    defaultValues,
    resolver: zodResolver(schema),
  });

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-4 bg-gray-100 p-4 rounded"
    >
      <div>
        <input
          {...register("title")}
          maxLength={255}
          placeholder="Lesson title"
          className="input w-full"
        />
        {errors.title && (
          <p className="text-sm text-red-600">{errors.title.message}</p>
        )}
      </div>

      <div>
        <input
          {...register("video_url")}
          placeholder="YouTube URL"
          className="input w-full"
        />
        {errors.video_url && (
          <p className="text-sm text-red-600">{errors.video_url.message}</p>
        )}
      </div>

      <button className="btn btn-primary">{submitLabel}</button>
    </form>
  );
}
