<template>
  <Navbar />
  <router-view />
  <Footer />
  <ModalUser />
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import ModalUser from "@/components/ModalUser.vue";

export default {
  components: {
    Navbar,
    Footer,
    ModalUser,
  },
  Loginounted() {
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
  --heght-nav: 65px;
  --font-family-sans-serif: -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif,
    "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
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
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
  font-size: 3.3rem;
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

.container {
  margin: 0 40px;
}

.title {
  text-align: center;
  margin-top: 30px;
}

.btn {
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  color: #fff;
  text-align: center;
  text-decoration: none;
  vertical-align: middle;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  background-color: transparent;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
</style>
