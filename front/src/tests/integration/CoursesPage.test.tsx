import { screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, test } from "vitest";
import CoursesPage from "../../pages/CoursesPage";
import { resetMockState } from "../mocks/handlers";
import { renderWithProviders } from "../testUtils";

beforeEach(resetMockState);

test("flujo de crear & lista curso (snapshot)", async () => {
  const { asFragment } = renderWithProviders(<CoursesPage />);
  const user = userEvent.setup();

  expect(asFragment()).toMatchSnapshot("CoursesPage-estado-inicial");

  await user.click(screen.getByRole("button", { name: /new course/i }));
  await user.type(screen.getByPlaceholderText(/title/i), "E2E");
  await user.type(screen.getByPlaceholderText(/description/i), "desc");
  await user.click(screen.getByRole("button", { name: /^save$/i }));

  await waitFor(() => expect(screen.getByText("E2E")).toBeInTheDocument());

  expect(asFragment()).toMatchSnapshot("CoursesPage-tras-crear-curso");
});

test("cancelar formulario vuelve al estado anterior", async () => {
  const { asFragment } = renderWithProviders(<CoursesPage />);
  const user = userEvent.setup();

  await user.click(screen.getByRole("button", { name: /new course/i }));
  expect(screen.getByRole("button", { name: /cancel/i })).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: /cancel/i }));
  expect(asFragment()).toMatchSnapshot("CoursesPage-cancelado");
});
