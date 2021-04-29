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
  addPost(data, imageFile) {
    const formData = new FormData();
    formData.append("title", data.title);
    formData.append("description", data.description);
    formData.append("content", data.content);
    formData.append("image", imageFile);
    formData.append("user", 1);

    return apiClient.post(`/api/add-post`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  },
  editPost(data, id, imageFile) {
    const formData = new FormData();
    formData.append("title", data.title);
    formData.append("description", data.description);
    formData.append("content", data.content);
    if (imageFile !== null) {
      formData.append("image", imageFile);
    }
    return apiClient.put(`/api/edit-post/${id}`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  },
};
