import { screen, waitFor, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, expect, test } from "vitest";
import { CoursesAPI } from "../../api/courses";
import CoursePage from "../../pages/CoursePage";
import { resetMockState } from "../mocks/handlers";
import { renderCourseRoute } from "../testUtils";

async function makeCourse() {
  const { data } = await CoursesAPI.create({
    title: "Initial",
    course_desc: "desc",
    instructor_id: 1,
  });
  return data.id;
}

beforeEach(resetMockState);

test("muestra info y permite actualizar título", async () => {
  const id = await makeCourse();
  const { asFragment } = renderCourseRoute(id, <CoursePage />);
  const user = userEvent.setup();

  await screen.findByText("Initial");

  await user.click(screen.getByRole("button", { name: /edit/i }));
  const titleInput = screen.getByPlaceholderText(/title/i);
  await user.clear(titleInput);
  await user.type(titleInput, "Updated!");
  await user.click(screen.getByRole("button", { name: /update/i }));

  await user.click(screen.getByRole("button", { name: /^save$/i }));

  await waitFor(() => expect(screen.getByText("Updated!")).toBeInTheDocument());

  expect(asFragment()).toMatchSnapshot("CoursePage-after-update");
});

test("agrega y elimina una lección", async () => {
  const id = await makeCourse();
  const { asFragment } = renderCourseRoute(id, <CoursePage />);
  const user = userEvent.setup();

  expect(asFragment()).toMatchSnapshot("CoursePage-before-add-lesson");

  await user.click(screen.getByRole("button", { name: /add lesson/i }));
  await user.type(screen.getByPlaceholderText(/lesson title/i), "L1");
  await user.type(
    screen.getByPlaceholderText(/youtube url/i),
    "https://www.youtube.com/watch?v=ABCDEFGHIJK"
  );
  await user.click(screen.getByRole("button", { name: /^save$/i }));

  await screen.findByText("L1");

  expect(asFragment()).toMatchSnapshot("CoursePage-after-add-lesson");

  const lessonHeading = await screen.findByText("L1", { selector: "h4" });
  const card = lessonHeading.closest("div");
  const deleteLessonBtn = within(card!).getByRole("button", {
    name: /^delete$/i,
  });

  await user.click(deleteLessonBtn);

  await screen.findByText(/delete lesson\?/i);

  expect(document.body).toMatchSnapshot("CoursePage-before-click-delete");

  const deleteButtons = screen.getAllByRole("button", { name: /^delete$/i });
  await user.click(deleteButtons[2]);
  await waitFor(() =>
    expect(screen.queryByText(/delete lesson\?/i)).not.toBeInTheDocument()
  );
  expect(asFragment()).toMatchSnapshot("CoursePage-after-click-delete");
});
