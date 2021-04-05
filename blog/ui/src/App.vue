<template>
  <Navbar />
  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div> -->
  <router-view />
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
};
</script>

<style>
@font-face {
  font-family: "Lato", sans-serif;
  src: local("Lato"), url("./assets/fonts/Lato/Lato-Light.ttf");
}

body {
  background-color: #333;
  color: #fff;
  font-family: "Lato", sans-serif;
  font-weight: 300;
  margin: 0;
}

h1 {
  margin: 0;
}
</style>
