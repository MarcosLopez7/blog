<template>
  <h1>Recents posts</h1>
  <div class="recent-post">
    <PostItem v-for="post in posts" :item="post" :key="post" />
  </div>
</template>

<script scoped>
import BackendServices from "@/services/BackendServices.js";

import PostItem from "@/components/PostItem.vue";

export default {
  components: {
    PostItem,
  },
  data() {
    return {
      posts: [],
    };
  },
  methods: {
    isVisible(post) {
      return post.visible;
    },
  },
  created() {
    BackendServices.getPosts().then((response) => {
      this.posts = response.data;
    });
  },
};
</script>

<style scoped>
.recent-post {
  padding: 1.4rem;
  width: calc(100% - 40px);
  max-width: 1350px;
  margin: 0 auto;
  margin-top: 10px;
  justify-content: center;
  flex-wrap: wrap;
  display: flex;
}

h1 {
  margin-top: 30px;
  text-align: center;
  font-size: 38px;
}

/* @media (max-width: 1374px) {
  .recent-post {
    max-width: 940px;
  }
} */
</style>
