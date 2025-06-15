import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render } from "@testing-library/react";
import type { ReactElement } from "react";
import { MemoryRouter, Route, Routes } from "react-router-dom";

function getClient() {
  return new QueryClient({ defaultOptions: { queries: { retry: false } } });
}

export function renderWithProviders(
  ui: ReactElement,
  { route = "/" }: { route?: string } = {}
) {
  return render(
    <MemoryRouter initialEntries={[route]}>
      <QueryClientProvider client={getClient()}>{ui}</QueryClientProvider>
    </MemoryRouter>
  );
}

export function renderCourseRoute(id: number, element: ReactElement) {
  return renderWithProviders(
    <Routes>
      <Route path="/courses/:id" element={element} />
    </Routes>,
    { route: `/courses/${id}` }
  );
}
