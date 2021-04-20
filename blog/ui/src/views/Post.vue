<template>
  <div class="post-container">
    <h1>{{ post.title }}</h1>
    <img :src="post.image" />
    <div class="post-info">
      {{ post.user.username }} <br />
      {{ dateFormatted }}
    </div>
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
  computed: {
    dateFormatted() {
      if (this.post.length === 0) {
        return "";
      } else {
        const date = new Date(this.post.date);
        return date;
      }
    },
  },
  created() {
    BackendServices.getPost(this.$route.params.id).then((response) => {
      this.post = response.data;
    });
  },
};
</script>

<style scoped>
@font-face {
  font-family: "Lato", sans-serif;
  src: local("Lato"), url("../assets/fonts/Lato/Lato-Regular.ttf");
}

.post-container h1 {
  font-family: "Lato", sans-serif !important;
}

.post-container {
  width: 800px;
  margin: 0 auto;
  margin-top: 30px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif,
    "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-weight: 400;
  line-height: 1.5;
}

.post-container img {
  width: 100%;
}

.post-info {
  font-size: smaller;
  color: #888;
  margin-top: 10px;
}
</style>
