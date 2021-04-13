<template>
  <nav class="nav">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/">Explore</a></li>
      <li><a href="/">Login</a></li>
    </ul>
  </nav>
</template>

<script></script>

<style scoped>
/* :root {
  --heght-nav: 50px;
} */

.nav {
  height: var(--heght-nav);
  padding: 10px 8px;
  background-color: var(--bg-color);
}

li {
  display: inline;
  float: left;
  margin: auto 0;
}

a {
  display: block;
  padding: 8px;
  font-weight: 550;
}

ul {
  margin-top: calc(var(--heght-nav) / 5);
}
</style>
