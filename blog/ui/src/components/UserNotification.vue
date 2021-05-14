<template>
  <div class="modal-body">
    <h4>La cuenta ha sido creada exitosamente</h4>
    <p>verifica tu cuenta en tu correó eletronico</p>
  </div>
  <div class="modal-footer">
    <button type="button" class="btn" @click="submit()">OK</button>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.modal-body {
  padding: 1rem 1rem;
  background-color: var(--bg-color);
  /* width: 100%; */
}

h4 {
  margin: 0;
  text-align: center;
  font-size: 24px;
}

p {
  padding-top: 5px;
  text-align: center;
  font-size: 18px;
}
</style>
