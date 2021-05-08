<template>
  <div
    id="loginModal"
    class="modal"
    :class="{ showingModal: showModal }"
    @click="hideModal($event)"
  >
    <Login v-if="$store.state.loginVisible" />
    <SignUp v-if="$store.state.signUpVisible" />
  </div>
</template>

<script>
import Login from "@/components/Login.vue";
import SignUp from "@/components/SignUp.vue";

export default {
  components: {
    Login,
    SignUp,
  },
  computed: {
    showModal() {
      return this.$store.state.loginVisible || this.$store.state.signUpVisible;
    },
  },
  methods: {
    hideModal(event) {
      if (event.target == document.getElementById("loginModal")) {
        if (this.$store.state.loginVisible) {
          this.$store.dispatch("changeLoginVisibility");
        } else if (this.$store.state.signUpVisible) {
          this.$store.dispatch("changeSignUpVisibility");
        }
      }
    },
  },
};
</script>

<style scoped>
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
</style>
