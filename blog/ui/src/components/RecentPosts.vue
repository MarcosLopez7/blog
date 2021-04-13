<template>
  <div class="recent-post">
    <h1>Recents posts</h1>

    <PostItem v-for="post in posts" :item="post" :key="post" />
  </div>
</template>

<script scoped>
import PostItem from "@/components/PostItem.vue";

export default {
  components: {
    PostItem,
  },
  data() {
    return {
      posts: [
        {
          title: "Post 1",
          image: "",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s text ever since the 1500s text ever since the 1500s text ever since the 1500s text ever since the 1500s text ever since the 1500s text ever since the 1500s text ever since the 1500s",
        },
        {
          title: "Post 2",
          image: "",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
        },
        {
          title: "Post 3",
          image: "",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
        },
        {
          title: "Post 4",
          image: "",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
        },
        {
          title: "Post 5",
          image: "",
          description:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
        },
      ],
    };
  },
};
</script>

<style scoped>
.recent-post {
  padding: 1.4rem;
  width: calc(100% - 40px);
  max-width: 1350px;
  margin: 0 auto;
}

.recent-post h1 {
  text-align: center;
  font-size: 38px;
}
</style>
