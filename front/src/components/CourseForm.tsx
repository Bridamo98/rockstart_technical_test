import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import * as z from "zod";

import { InstructorsAPI } from "../api/instructors";
import type { Instructor } from "../types";

const createSchema = z.object({
  title: z
    .string()
    .min(1, "Title is required")
    .max(255, "Title must be ≤ 255 characters"),
  course_desc: z.string().min(1, "Description is required"),
  instructor_id: z.number().int().positive("Select instructor"),
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

export default function CourseForm({
  defaultValues,
  onSubmit,
  submitLabel = "Save",
}: Props) {
  const isEdit = !!defaultValues;
  const schema = isEdit ? updateSchema : createSchema;

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm<FormData>({
    defaultValues,
    resolver: zodResolver(schema),
  });

  const [instructors, setInstructors] = useState<Instructor[]>([]);

  useEffect(() => {
    InstructorsAPI.list().then((r) => {
      setInstructors(r.data);
      if (!defaultValues?.instructor_id && r.data.length > 0) {
        setValue("instructor_id", r.data[0].id);
      }
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-4 bg-white p-4 rounded shadow"
    >
      <div>
        <input
          {...register("title")}
          maxLength={255}
          placeholder="Title"
          className="input w-full"
        />
        {errors.title && (
          <p className="text-sm text-red-600">{errors.title.message}</p>
        )}
      </div>
      <div>
        <textarea
          {...register("course_desc")}
          placeholder="Description"
          className="textarea w-full"
        />
        {errors.course_desc && (
          <p className="text-sm text-red-600">{errors.course_desc.message}</p>
        )}
      </div>
      <div>
        <select {...register("instructor_id")} className="select w-full">
          {instructors.map((i) => (
            <option key={i.id} value={i.id}>
              {i.name}
            </option>
          ))}
        </select>
        {errors.instructor_id && (
          <p className="text-sm text-red-600">{errors.instructor_id.message}</p>
        )}
      </div>

      <button className="btn btn-primary">{submitLabel}</button>
    </form>
  );
}
