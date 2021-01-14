import http from "./httpService";
import { apiUrl } from "../config.json";
import jwtDecode from "jwt-decode";

const apiEndPoint = apiUrl + "/usr/auth/";

export async function login(username, password) {
  const { data: jwt } = await http.post(apiEndPoint, { username, password });
  localStorage.setItem("token", jwt["access"]);
}

export function logout() {
  localStorage.removeItem("token");
}

export function getCurrentUser() {
  try {
    const jwt = localStorage.getItem("token");
    return jwtDecode(jwt);
  } catch (error) {
    return null;
  }
}

export default {
  login,
  logout,
  getCurrentUser,
};
