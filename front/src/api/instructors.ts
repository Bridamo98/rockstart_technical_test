import type { Instructor } from "../types";
import { api } from "./client";

export const InstructorsAPI = {
  list: () => api.get<Instructor[]>("/instructors/"),
};
