import "@testing-library/jest-dom";
import { afterAll, afterEach, beforeAll } from "vitest";
import { resetMockState } from "./tests/mocks/handlers";
import { server } from "./tests/mocks/server";

beforeAll(() => server.listen());
afterEach(() => {
  server.resetHandlers();
  resetMockState();
});
afterAll(() => server.close());
