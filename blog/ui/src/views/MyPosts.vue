<template>
  <div class="container">
    <h1 class="title">My posts</h1>

    <PostZakvil v-for="post in posts" :key="post" :post="post" />
  </div>
</template>

<script>
import BackendServices from "@/services/BackendServices.js";
import PostZakvil from "@/components/PostZakvil.vue";

export default {
  components: {
    PostZakvil,
  },
  data() {
    return {
      posts: [],
    };
  },
  created() {
    BackendServices.getMyPosts(1).then((response) => {
      this.posts = response.data;
    });
  },
};
</script>
