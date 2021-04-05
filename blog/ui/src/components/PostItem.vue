<template>
  <div>
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
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
div {
  background-color: seagreen;
  height: 300px;
  width: 400px;
  display: inline-block;
  margin: 20px 20px;
}
</style>
