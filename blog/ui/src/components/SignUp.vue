<template>
  <!-- <div class="modal-content">
    <div class="modal-header">
      <span> </span>
      <h2>Sign Up</h2>
      <span> </span>
      <span class="close" @click="hideModal()">&times;</span>
    </div> -->
  <div class="modal-body">
    <form class="form">
      <div class="field-area">
        <input
          type="text"
          class="input-form"
          v-model="username"
          placeholder="Username"
          required
        />
      </div>
      <div class="field-area">
        <input
          type="email"
          class="input-form"
          v-model="email"
          placeholder="Email"
          required
        />
      </div>
      <div class="field-area">
        <input
          type="password"
          class="input-form"
          v-model="password"
          placeholder="Password"
          required
        />
      </div>
    </form>
  </div>
  <div class="modal-footer">
    <button type="button" class="btn" @click="submit()">Submit</button>
  </div>
  <!-- </div> -->
</template>

<script>
// import BackendServices from "@/services/BackendServices.js";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  methods: {
    submit() {
      this.$store.dispatch("setIsUserCreated", true);
      // const data = {
      //   username: this.username,
      //   email: this.email,
      //   password: this.password,
      // };
      // BackendServices.createUser(data)
      //   .then((response) => {
      //     console.log(response.data);
      //     this.$store.dispatch("setIsUserCreated", true);
      //     this.username = "";
      //     this.email = "";
      //     this.password = "";
      //   })
      //   .catch((error) => {
      //     console.error(error.response);
      //   });
    },
  },
};
</script>

<style>
.close {
  flex-flow: row;
}

.form {
  align-items: center;
  display: flex;
  flex-flow: column wrap;
  background-color: var(--bg-color);
  margin: 0 auto;
  border-radius: 5px;
  padding: 20px 10px;
}

.field-area {
  margin: 15px 0;
  max-width: 800px;
}
.field-area input {
  height: 30px;
  width: 390px;
}

.input-form {
  width: 100%;
  font-size: 1.3rem;
  border-radius: 5px;
  border-color: var(--bg-card);
  border-width: 2px;
  padding-left: 10px;
}

.modal-footer {
  background-color: var(--bg-color);
  padding: 1rem 1rem;
  align-items: center;
  display: flex;
  flex-flow: column wrap;
}

.modal-footer button {
  width: 400px;
  background-color: var(--bg-card);
  margin: 0 auto;
  font-size: 18px;
  font-weight: 600;
}

.forgot-password {
  margin-top: 20px;
}
</style>
