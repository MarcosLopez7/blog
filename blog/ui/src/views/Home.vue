<template>
  <div>
    <div class="main-image">
      <div class="image-containter">
        <div class="image-containter-item">
          <h1>Welcome to Pylord's Blog</h1>
        </div>
        <div class="image-containter-item">
          <p>
            HI, my name is Marcos López, in social network I’m as Pylord. I’m
            software developer with 5 years of professional experience, I love
            develop things that can solve problems or be helpful for people or
            companies. I have been working in Kantar as Web developer since 3
            years ago, we develop web applications oriented to data science for
            satisfy Kantar operations requirements and delivery products to our
            clients.
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

<style scoped>
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
  line-height: 1.8;
  font-size: 1.25rem;
}

.image-containter h1 {
  margin-top: 1rem;
  font-size: 48px;
}
</style>
