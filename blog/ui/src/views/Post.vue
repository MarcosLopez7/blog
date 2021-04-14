<template>
  <div class="post">
    <h1>{{ post.title }}</h1>
    <img :src="post.image" />
    <div class="post-content" v-html="post.content"></div>
  </div>
</template>

<script>
import BackendServices from "@/services/BackendServices.js";

export default {
  data() {
    return {
      post: {},
    };
  },
  created() {
    BackendServices.getPost(this.$route.params.id).then((response) => {
      this.post = response.data;
    });
  },
};
</script>

<style scoped></style>
