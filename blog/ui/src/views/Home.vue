<template>
  <div>
    <div class="main-image">
      <div class="image-containter">
        <div class="image-containter-item">
          <h1>Pylord's Blog</h1>
        </div>
        <div class="image-containter-item">
          <p>
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book. It has survived not
            only five five centuries, but also the leap into electronic
            typesetting, remaining essentially unchanged. It was popularised in
            the 1960s with the release of Letraset sheets containing Lorem Ipsum
            passages, and more recently with desktop publishing software like
            Aldus PageMaker including versions of Lorem Ipsum.
          </p>
        </div>
      </div>
    </div>
    <RecentPosts />
  </div>
</template>

<script scoped>
import RecentPosts from "@/components/RecentPosts.vue";

export default {
  components: {
    RecentPosts,
  },
};
</script>

<style>
p {
  width: 50%;
}

.main-image {
  background-image: url("../assets/images/pexels-paras-katwal-4218883.jpg");
  width: 100%;
  height: 500px;
  background-size: cover;
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
}

.image-containter {
  background: rgba(0, 0, 0, 0.7);
  height: 100%;
  padding: 0 1rem;
}

.image-containter-item {
  display: inline-block;
  margin-top: 1rem;
  text-align: justify;
  text-justify: inter-word;
  line-height: 1.5;
}

.image-containter h1 {
  margin-top: 1rem;
  font-size: 48px;
}
</style>
