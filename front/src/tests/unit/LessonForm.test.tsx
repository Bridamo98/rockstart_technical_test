import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";
import LessonForm from "../../components/LessonForm";

it("rechaza url que no sea de YouTube (snapshot)", async () => {
  const { asFragment } = render(<LessonForm onSubmit={vi.fn()} />);
  const user = userEvent.setup();

  await user.type(screen.getByPlaceholderText(/lesson title/i), "L1");
  await user.type(
    screen.getByPlaceholderText(/youtube url/i),
    "https://vimeo.com/123"
  );
  await user.click(screen.getByRole("button", { name: /save/i }));

  expect(
    await screen.findByText(/must be a youtube link/i)
  ).toBeInTheDocument();

  expect(asFragment()).toMatchSnapshot();
});
