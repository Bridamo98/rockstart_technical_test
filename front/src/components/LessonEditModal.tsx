import { useEffect, useState } from "react";
import { createPortal } from "react-dom";
import type { Lesson, LessonUpdateDTO } from "../types";
import ConfirmModal from "./ConfirmModal";
import LessonForm from "./LessonForm";

interface Props {
  open: boolean;
  lesson: Lesson | null;
  onClose: () => void;
  onSave: (changes: LessonUpdateDTO) => void;
}

export default function LessonEditModal({
  open,
  lesson,
  onClose,
  onSave,
}: Props) {
  const [pending, setPending] = useState<LessonUpdateDTO | null>(null);
  useEffect(() => {
    const onEsc = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", onEsc);
    return () => document.removeEventListener("keydown", onEsc);
  }, []);

  if (!open || !lesson) return null;

  return createPortal(
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded shadow w-full max-w-lg space-y-4">
        <h3 className="text-xl font-semibold">Edit lesson</h3>
        <LessonForm
          defaultValues={lesson}
          onSubmit={(vals) => setPending(vals)}
          submitLabel="Update"
        />
        <button onClick={onClose} className="btn btn-secondary w-full">
          Close
        </button>
      </div>
      <ConfirmModal
        open={!!pending}
        title="Save changes?"
        message="This will overwrite the existing lesson."
        confirmLabel="Save"
        onCancel={() => setPending(null)}
        onConfirm={() => {
          onSave(pending!);
          setPending(null);
        }}
      />
    </div>,
    document.body
  );
}
