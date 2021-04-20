<template>
  <a :href="`/post/${post.id}`">
    <div class="inline-post">
      <img :src="'http://127.0.0.1:8000' + post.image" />
      <div class="post-name">
        <h3>{{ post.title }}</h3>
      </div>
    </div>
  </a>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.inline-post {
  margin: 30px 0;
}

.inline-post img {
  width: 75px;
  display: inline-block;
  /* height: 50px; */
}

.post-name {
  margin-left: 30px;
  display: inline-block;
}

.post-name h3 {
  margin-top: -15px;
}
</style>
