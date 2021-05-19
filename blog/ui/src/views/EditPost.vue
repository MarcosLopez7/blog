<template>
  <article class="title">
    <h1>Edit Post</h1>
    <PostForm :edit="true" />
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
