import type { Lesson } from "../types";
import VideoPlayer from "./VideoPlayer";

interface Props {
  lesson: Lesson;
  onEdit: () => void;
  onDelete: () => void;
}
export default function LessonItem({ lesson, onEdit, onDelete }: Props) {
  return (
    <div className="bg-white p-4 rounded shadow space-y-2">
      <h4 className="font-bold">{lesson.title}</h4>
      <VideoPlayer url={lesson.video_url} />
      <div className="flex gap-2">
        <button onClick={onEdit} className="btn btn-sm btn-secondary">
          Edit
        </button>
        <button onClick={onDelete} className="btn btn-sm btn-error">
          Delete
        </button>
      </div>
    </div>
  );
}
