<template>
  <div class="title">
    <h1>Edit Post</h1>
    <PostForm :edit="true" />
  </div>
</template>

<script>
import PostForm from "@/components/PostForm.vue";

export default {
  components: {
    PostForm,
  },
};
</script>
