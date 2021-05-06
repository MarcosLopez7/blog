<template>
  <div id="loginModal" class="modal" :class="{ showingModal: showModal }">
    <div class="modal-content">
      <div class="modal-title">
        <h2>Login</h2>
        <span class="close" @click="hideModal()">&times;</span>
      </div>
      <div class="modal-body">
        <p>Hola soy el modal y soy chido</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    showModal() {
      return this.$store.state.loginVisible;
    },
  },
  methods: {
    hideModal() {
      this.$store.dispatch("changeVisibility");
    },
  },
};
</script>

<style>
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}

.showingModal {
  display: block;
}

.modal-content {
  background-color: var(--bg-color);
  margin: auto;
  padding: 20px;
  border: 1px solid var(--bg-card);
  width: 50%;
  border-radius: 5px;
}

.modal-title {
  font-size: 1.5rem;
  display: flex;
  flex-flow: row;
}

.modal-title h2 {
  margin: 0;
}

.close {
  flex-flow: row;
}
</style>
