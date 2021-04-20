import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/";

const apiClient = axios.create({
  baseURL: BASE_URL,
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  getPosts() {
    return apiClient.get(`/api/posts`);
  },
  getPost(id) {
    return apiClient.get(`/api/post/${id}`);
  },
  getMyPosts(id) {
    return apiClient.get(`/api/user-posts/${id}`);
  },
};
