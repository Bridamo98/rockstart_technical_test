import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, test, vi } from "vitest";
import CourseForm from "../../components/CourseForm";

test("UI inicial coincide con snapshot", () => {
  const { asFragment } = render(<CourseForm onSubmit={vi.fn()} />);
  expect(asFragment()).toMatchSnapshot();
});

test("muestra errores si se envía vacío", async () => {
  const onSubmit = vi.fn();
  const { asFragment } = render(<CourseForm onSubmit={onSubmit} />);
  const user = userEvent.setup();

  await user.click(screen.getByRole("button", { name: /save/i }));

  expect(await screen.findByText(/title is required/i)).toBeInTheDocument();
  expect(asFragment()).toMatchSnapshot("CourseForm-con-errores");
  expect(onSubmit).not.toHaveBeenCalled();
});
