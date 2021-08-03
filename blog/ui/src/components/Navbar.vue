<template>
  <nav class="nav">
    <div class="menu-nav">
      <ul>
        <li class="logo"><a href="/">Pylord</a></li>
        <li><a href="/about-me">About me</a></li>
        <li><a href="/">About this site</a></li>
        <li><a href="/">Contact</a></li>
        <li @click="showLogin()"><span>Login</span></li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  methods: {
    showLogin() {
      this.$store.dispatch("changeLoginVisibility");
    },
    showSignUp() {
      this.$store.dispatch("changeSignUpVisibility");
    },
  },
};
</script>

<style scoped>
/* :root {
  --heght-nav: 50px;
} */

.nav {
  height: var(--heght-nav);
  padding: 10px 8px;
  background-color: var(--bg-color);
  text-align: center;
}

li {
  margin: auto 8px;
}

a {
  display: block;
  padding: 8px;
  font-weight: 550;
  font-size: 1.5rem;
}

span {
  display: block;
  padding: 8px;
  font-weight: 550;
  font-size: 1.5rem;
}

ul {
  display: inline-flex;
  margin-top: calc(var(--heght-nav) / 5);
}

.logo a {
  margin-top: -6px;
  font-size: 2rem;
  color: var(--bg-card);
}

.menu-nav {
  margin: 0 auto;
}
</style>
