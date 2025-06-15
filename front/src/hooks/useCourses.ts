import { useEffect, useState } from "react";
import { CoursesAPI } from "../api/courses";
import type { Course } from "../types";

export default function useCourses() {
  const [data, setData] = useState<Course[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  const refresh = () =>
    CoursesAPI.list()
      .then((r) => setData(r.data))
      .finally(() => setLoading(false));

  useEffect(() => {
    refresh();
  }, []);

  return { courses: data, loading, refresh };
}
