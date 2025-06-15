import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { CoursesAPI } from "../api/courses";
import { LessonsAPI } from "../api/lessons";
import ConfirmModal from "../components/ConfirmModal";
import CourseForm from "../components/CourseForm";
import LessonEditModal from "../components/LessonEditModal";
import LessonForm from "../components/LessonForm";
import LessonItem from "../components/LessonItem";
import type {
  Course,
  Lesson,
  LessonCreateDTO,
  LessonUpdateDTO,
} from "../types";

export default function CoursePage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const courseId = Number(id);
  const [course, setCourse] = useState<Course | null>(null);
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [editMode, setEditMode] = useState(false);
  const [showLessonForm, setShowLessonForm] = useState(false);
  const [editingLesson, setEditingLesson] = useState<Lesson | null>(null);
  const [confirmDeleteCourse, setConfirmDeleteCourse] = useState(false);
  const [lessonToDelete, setLessonToDelete] = useState<Lesson | null>(null);
  const [pendingCourseChanges, setPendingCourseChanges] =
    useState<Partial<Course> | null>(null);

  const saveLesson = (changes: LessonUpdateDTO) =>
    editingLesson &&
    LessonsAPI.update(courseId, editingLesson.id, changes).then(() => {
      setEditingLesson(null);
      fetchAll();
    });

  const fetchAll = () => {
    CoursesAPI.get(courseId).then((r) => setCourse(r.data));
    LessonsAPI.list(courseId).then((r) => setLessons(r.data));
  };

  useEffect(() => {
    fetchAll();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const askUpdateCourse = (data: Partial<Course>) =>
    setPendingCourseChanges(data);

  const updateCourse = (data: Partial<Course>) =>
    CoursesAPI.update(courseId, data)
      .then(fetchAll)
      .then(() => setEditMode(false));

  const deleteCourse = () =>
    CoursesAPI.remove(courseId).then(() => navigate("/courses"));

  const addLesson = (formData: { title?: string; video_url?: string }) => {
    if (!formData.title || !formData.video_url) {
      return;
    }
    const data: LessonCreateDTO = {
      title: formData.title,
      video_url: formData.video_url,
    };
    return LessonsAPI.create(courseId, data)
      .then(fetchAll)
      .then(() => setShowLessonForm(false));
  };

  const delLesson = (lessonId: number) =>
    LessonsAPI.remove(courseId, lessonId).then(fetchAll);

  return (
    <div className="container mx-auto p-6 space-y-6">
      <button
        onClick={() => navigate("/courses")}
        className="btn btn-outline mb-4"
      >
        ← Back to Courses
      </button>
      {course && (
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold">{course.title}</h1>
          </div>
          <div className="space-x-2">
            {!editMode && (
              <>
                <button
                  onClick={() => setEditMode(true)}
                  className="btn btn-secondary"
                >
                  Edit
                </button>
                <button
                  onClick={() => setConfirmDeleteCourse(true)}
                  className="btn btn-error"
                >
                  Delete
                </button>
              </>
            )}
            {editMode && (
              <button
                onClick={() => setEditMode(false)}
                className="btn btn-outline"
              >
                Cancel
              </button>
            )}
          </div>
        </div>
      )}

      {course && !editMode && <p>{course.course_desc}</p>}

      {editMode && course && (
        <CourseForm
          defaultValues={course as Course}
          onSubmit={askUpdateCourse}
          submitLabel="Update"
        />
      )}

      <hr />

      <div className="flex items-center justify-between">
        <h2 className="text-xl font-semibold">Lessons</h2>
        <button
          onClick={() => setShowLessonForm(!showLessonForm)}
          className="btn btn-primary"
        >
          {showLessonForm ? "Cancel" : "Add lesson"}
        </button>
      </div>

      {showLessonForm && <LessonForm onSubmit={addLesson} />}

      <div className="grid md:grid-cols-2 gap-4">
        {lessons.map((l) => (
          <LessonItem
            key={l.id}
            lesson={l}
            onEdit={() => setEditingLesson(l)}
            onDelete={() => setLessonToDelete(l)}
          />
        ))}
      </div>
      <LessonEditModal
        open={!!editingLesson}
        lesson={editingLesson}
        onClose={() => setEditingLesson(null)}
        onSave={saveLesson}
      />
      <ConfirmModal
        open={confirmDeleteCourse}
        title="Delete course?"
        message="This action cannot be undone."
        confirmLabel="Delete"
        onCancel={() => setConfirmDeleteCourse(false)}
        onConfirm={() => {
          setConfirmDeleteCourse(false);
          deleteCourse();
        }}
      />
      <ConfirmModal
        open={!!pendingCourseChanges}
        title="Save changes?"
        message="Modify course details?"
        confirmLabel="Save"
        onCancel={() => setPendingCourseChanges(null)}
        onConfirm={() => {
          updateCourse(pendingCourseChanges!);
          setPendingCourseChanges(null);
        }}
      />
      <ConfirmModal
        open={!!lessonToDelete}
        title="Delete lesson?"
        message={`"${lessonToDelete?.title}" will be removed.`}
        confirmLabel="Delete"
        onCancel={() => setLessonToDelete(null)}
        onConfirm={() => {
          delLesson(lessonToDelete!.id);
          setLessonToDelete(null);
        }}
      />
    </div>
  );
}
