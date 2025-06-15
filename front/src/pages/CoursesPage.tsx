import { useState } from "react";
import { CoursesAPI } from "../api/courses";
import CourseForm from "../components/CourseForm";
import CourseList from "../components/CourseList";
import useCourses from "../hooks/useCourses";
import type { CourseCreateDTO } from "../types";

export default function CoursesPage() {
  const { courses, loading, refresh } = useCourses();
  const [showForm, setShowForm] = useState(false);

  const addCourse = (values: {
    title?: string;
    course_desc?: string;
    instructor_id?: number;
  }) => {
    if (
      !values.title ||
      !values.course_desc ||
      values.instructor_id === undefined
    ) {
      return;
    }
    const data: CourseCreateDTO = {
      title: values.title,
      course_desc: values.course_desc,
      instructor_id: values.instructor_id,
    };
    return CoursesAPI.create(data).then(() => {
      setShowForm(false);
      refresh();
    });
  };

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-4">Courses</h1>
      <button
        onClick={() => setShowForm(!showForm)}
        className="btn btn-primary mb-4"
      >
        {showForm ? "Cancel" : "New course"}
      </button>

      {showForm && <CourseForm onSubmit={addCourse} />}

      {loading ? <p>Loading …</p> : <CourseList courses={courses} />}
    </div>
  );
}
