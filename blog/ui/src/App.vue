<template>
  <Navbar />
  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div> -->
  <router-view />
  <Footer />
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Navbar,
    Footer,
  },
  mounted() {
    const recaptchaScript = document.createElement("script");
    recaptchaScript.setAttribute(
      "src",
      "https://use.fontawesome.com/aa4ffc396e.js"
    );
    document.head.appendChild(recaptchaScript);
  },
};
</script>

<style>
:root {
  --bg-color: #222;
  --bg-card: #208aae;
  --color-text: #fff;
  --heght-nav: 50px;
}

@font-face {
  font-family: "Lato", sans-serif;
  src: local("Lato"), url("./assets/fonts/Lato/Lato-Regular.ttf");
}

body {
  background-color: var(--bg-color);
  color: var(--color-text);
  font-family: "Lato", sans-serif;
  font-weight: 300;
  margin: 0;
}

h1 {
  margin: 0;
}

a {
  color: var(--color-text);
  text-decoration: none;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
</style>
