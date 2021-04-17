<template>
  <nav class="nav">
    <div class="menu-nav">
      <ul>
        <li class="logo"><a href="/">Pylord</a></li>
        <li><a href="/">Explore</a></li>
        <li><a href="/">About me</a></li>
        <li><a href="/">Login</a></li>
      </ul>
    </div>
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
