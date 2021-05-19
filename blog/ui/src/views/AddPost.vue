<template>
  <article class="title">
    <h1>Create Post</h1>
    <PostForm :edit="false" />
  </article>
</template>

<script>
import PostForm from "@/components/PostForm.vue";

export default {
  components: {
    PostForm,
  },
};
</script>
