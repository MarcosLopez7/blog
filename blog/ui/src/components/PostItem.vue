<template>
  <div class="post-card">
    <div class="image-card"></div>
    <h3>{{ item.title }}</h3>
    <p class="block-ellipsis">{{ item.description }}</p>
  </div>
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
  line-height: 1;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.image-card {
  background-image: url("http://localhost:8000/static/img/prueba_ShFirVO.jpg");
  background-color: white;
  width: 100%;
  height: 200px;
}
</style>
