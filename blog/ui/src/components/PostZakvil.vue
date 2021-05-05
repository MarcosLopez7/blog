<template>
  <div class="inline-post">
    <a :href="`/post/${post.id}`">
      <img :src="'http://127.0.0.1:8000' + post.image" />
    </a>
    <div class="post-name">
      <a :href="`/post/${post.id}`">
        <h3>{{ post.title }}</h3>
      </a>
    </div>
    <div class="post-buttons">
      <a :href="`/edit-post/${post.id}`">
        <button class="btn" type="button">
          <i class="fa fa-pencil-square-o" aria-hidden="true"></i>
        </button>
      </a>

      <button class="btn" type="button">
        <i class="fa fa-eye-slash" aria-hidden="true"></i>
      </button>
    </div>
  </div>
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
  margin: 10px 0;
  /* background-color: aqua; */
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 10px;
  background: #222222;
  box-shadow: 20px 20px 60px #1d1d1d, -20px -20px 60px #272727;
}

.inline-post img {
  padding: 5px 5px;
  width: 75px;
  height: 45px;
  display: inline-block;
  /* height: 50px; */
}

.post-name {
  margin-left: 30px;
  display: inline-block;
}

.post-buttons button {
  background-color: rgba(153, 153, 153, 0.5);
  border-color: rgba(153, 153, 153, 0.5);
  margin: 0 5px;
}

.post-buttons button:hover {
  background-color: rgba(121, 121, 121, 0.5);
  border-color: rgba(121, 121, 121, 0.5);
  margin: 0 5px;
}
</style>
