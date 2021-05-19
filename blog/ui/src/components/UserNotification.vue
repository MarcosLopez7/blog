<template>
  <div class="modal-body">
    <h4>La cuenta ha sido creada exitosamente</h4>
    <p>
      Te hemos mandado un correo electrónico para que lo verifiques, sino está
      en tu buzón de entrada verifica en la carpeta de spam
    </p>
  </div>
  <div class="modal-footer">
    <button
      type="button"
      class="btn"
      @click="$store.dispatch('setIsUserCreated', false)"
    >
      OK
    </button>
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
