<template>
  <article class="post-card" v-if="item.visible">
    <a :href="`/post/${item.id}`">
      <!-- <div
      class="image-card"
      v-bind:style="{ 'background-image': `url('${item.image}')` }"
    ></div> -->
      <figure>
        <img class="image-card" :src="item.image" :alt="item.title" />
      </figure>
      <h3>{{ item.title }}</h3>
      <p class="block-ellipsis">{{ item.description }}</p>
    </a>
  </article>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.post-card {
  background-color: var(--bg-card);
  /* background-color: #fff;
  color: #333; */
  height: 400px;
  width: 400px;
  display: inline-block;
  margin: 20px 20px;
  border-radius: 5px;
}

.post-card h3 {
  font-size: 1.8rem;
  margin-left: 20px;
}

/* .post-card p {
  font-size: 1rem;
  width: calc(100% - 40px);
  margin: 0 auto;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 75px;
  overflow-wrap: break-word;
} */

.block-ellipsis {
  display: block;
  display: -webkit-box;
  max-width: 100%;
  width: calc(100% - 40px);
  height: 70px;
  margin: 0 auto;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.image-card {
  background-color: white;
  width: 100%;
  height: 200px;
  border-radius: 5px 5px 0 0;
}
</style>
