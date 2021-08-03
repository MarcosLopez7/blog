<template>
  <div class="about-me">
    <div class="header-about-me">
      <div class="about-me-image"></div>
      <div class="info"><h1>About me</h1></div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.header-about-me {
  padding: 0 40px;
}

.about-me-image {
  background-image: url("../assets/images/yo.jpg");
  width: 300px;
  height: 350px;
  background-size: cover;
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
}
</style>
