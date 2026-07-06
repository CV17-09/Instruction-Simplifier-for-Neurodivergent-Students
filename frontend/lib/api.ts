import axios from "axios";

const API_URL = "http://localhost:8000";

export async function simplifyAssignment(text: string) {
  const response = await axios.post(`${API_URL}/simplify`, {
    text,
  });

  return response.data;
}