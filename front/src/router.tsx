import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import CoursePage from "./pages/CoursePage";
import CoursesPage from "./pages/CoursesPage";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/courses" />} />
        <Route path="/courses" element={<CoursesPage />} />
        <Route path="/courses/:id" element={<CoursePage />} />
      </Routes>
    </BrowserRouter>
  );
}
