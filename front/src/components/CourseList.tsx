import { Link } from "react-router-dom";
import type { Course } from "../types";

type Props = { courses: Course[] };

export default function CourseList({ courses }: Props) {
  return (
    <ul className="space-y-2">
      {courses.map((c) => (
        <li key={c.id} className="p-4 bg-white rounded shadow hover:bg-gray-50">
          <Link to={`/courses/${c.id}`}>
            <h2 className="font-semibold">{c.title}</h2>
            <p className="text-sm text-gray-600">{c.course_desc}</p>
          </Link>
        </li>
      ))}
    </ul>
  );
}
