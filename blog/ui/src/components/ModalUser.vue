<template>
  <div
    id="loginModal"
    class="modal"
    :class="{ showingModal: showModal }"
    @click="hideModal($event)"
  >
    <div class="modal-content">
      <div class="modal-header">
        <span> </span>
        <div
          class="tab-modal"
          :class="{ selected: showingLogin }"
          @click="showingLogin = true"
        >
          <h2>Login</h2>
        </div>
        <div
          class="tab-modal"
          :class="{ selected: showingSignUp }"
          @click="showingLogin = false"
        >
          <h2>Sign Up</h2>
        </div>
        <span> </span>
        <!-- <span class="close" @click="hideModal()">&times;</span> -->
      </div>
      <Login v-if="showingLogin && !$store.state.isUserCreated" />
      <SignUp v-if="!showingLogin && !$store.state.isUserCreated" />
      <UserNotifification v-if="$store.state.isUserCreated" />
    </div>
  </div>
</template>

<script>
import Login from "@/components/Login.vue";
import SignUp from "@/components/SignUp.vue";
import UserNotifification from "@/components/UserNotification.vue";

export default {
  components: {
    Login,
    SignUp,
    UserNotifification,
  },
  data() {
    return {
      showingLogin: true,
    };
  },
  computed: {
    showModal() {
      return this.$store.state.loginVisible || this.$store.state.signUpVisible;
    },
    showingSignUp() {
      return !this.showingLogin;
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

.modal-content {
  /* background-color: var(--bg-card); */
  margin: auto;
  border: 1px solid var(--bg-card);
  width: 500px;
  border-radius: 5px;
}

.modal-header {
  font-size: 1.5rem;
  display: flex;
  flex-shrink: 0;
  align-items: center;
  justify-content: space-between;
  /* padding: 1rem 1rem; */
}

.modal .tab-modal {
  cursor: pointer;
  width: 100%;
  padding: 1rem 1rem;
  /* opacity: 0.5; */
  background-color: rgba(0, 106, 132);
  color: #888;
}

.modal .tab-modal:hover {
  background-color: aquamarine;
  color: #fff;
}

/* TODO Quitar important con Victor o con Pamsho */
.selected {
  background-color: rgba(32, 138, 174) !important;
  color: #fff !important;
  cursor: unset !important;
}

.modal-header h2 {
  margin: 0;
  text-align: center;
}
</style>
