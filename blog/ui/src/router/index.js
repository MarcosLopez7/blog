import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Post from "@/views/Post.vue";
import MyPosts from "@/views/MyPosts.vue";
import AddPost from "@/views/AddPost.vue";
import EditPost from "@/views/EditPost.vue";
import AboutMe from "@/views/AboutMe.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/post/:id",
    name: "Post",
    component: Post,
  },
  {
    path: "/my-posts",
    name: "MyPosts",
    component: MyPosts,
  },
  {
    path: "/add-post",
    name: "AddPost",
    component: AddPost,
  },
  {
    path: "/about-me",
    name: "AboutMe",
    component: AboutMe,
  },
  {
    path: "/edit-post/:id",
    name: "EditPost",
    component: EditPost,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
