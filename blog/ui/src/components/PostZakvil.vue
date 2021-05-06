<template>
  <div class="inline-post">
    <a :href="`/post/${post.id}`">
      <div class="image-visible-overlay">
        <img
          :src="'http://127.0.0.1:8000' + post.image"
          :class="{ imgInvisible: !post.visible }"
        />
        <i v-if="!post.visible" class="fa fa-eye-slash" aria-hidden="true"></i>
      </div>
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

      <button class="btn" type="button" @click="changeVisibility(post)">
        <i v-if="!post.visible" class="fa fa-eye" aria-hidden="true"></i>
        <i v-if="post.visible" class="fa fa-eye-slash" aria-hidden="true"></i>
      </button>
    </div>
  </div>
</template>

<script>
import BackendServices from "@/services/BackendServices.js";

export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  methods: {
    changeVisibility(post) {
      BackendServices.editVisiblePost(!post.visible, post.id)
        .then((response) => {
          post.visible = response.data.visible;
        })
        .catch((response) => {
          console.error(response.error);
        });
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

.image-visible-overlay {
  position: relative;
}

.image-visible-overlay i {
  position: absolute;
  top: 12.5px;
  left: 29px;
  font-size: 1.8rem;
}

.imgInvisible {
  opacity: 0.3;
}
</style>
