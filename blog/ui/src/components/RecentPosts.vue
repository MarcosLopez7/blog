<template>
  <div class="recent-post">
    <h1>Recents posts</h1>

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
  margin-top: 30px;
}

.recent-post h1 {
  text-align: center;
  font-size: 38px;
}

@media (max-width: 1374px) {
  .recent-post {
    max-width: 940px;
  }
}
</style>
