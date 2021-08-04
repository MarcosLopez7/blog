<template>
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
import BackendServices from "@/services/BackendServices.js";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      errors: [],
    };
  },
  methods: {
    submit() {
      this.errors = [];
      if (!this.validate()) {
        return;
      }

      const data = {
        username: this.username,
        email: this.email,
        password: this.password,
      };
      BackendServices.createUser(data)
        .then((response) => {
          console.log(response.data);
          this.$store.dispatch("setIsUserCreated", true);
          this.$store.dispatch("changeLoginVisibility");
          this.username = "";
          this.email = "";
          this.password = "";
        })
        .catch((error) => {
          console.error(error.response);
        });
    },
    validate() {
      const validatePattern = /^[a-zA-Z0-9_@.+-]+$/;
      const validateIfNotNumPattern = /^[0-9]+$/;

      if (!this.username) {
        this.errors.push("The username is required");
      }

      if (!this.email) {
        this.errors.push("The email is required");
      }

      if (!this.password) {
        this.errors.push("The password is required");
      }

      if (this.username.length > 150) {
        this.errors.push("The username should be 150 characters or fewer");
      }

      if (!validatePattern.test(this.username)) {
        this.errors.push(
          "Letters, digits and @/./+/-/_ are the only allowed characters."
        );
      }

      if (this.email.length > 150) {
        this.errors.push("The email should be 150 characters or fewer");
      }

      if (!this.validEmail(this.email)) {
        this.errors.push("Please ionsert a valid email");
      }

      if (this.password.length < 8) {
        this.errors.push("The password should be 8 characters or more");
      }

      if (validateIfNotNumPattern.test(this.password)) {
        this.errors.push("The password should not be only numbers");
      }

      if (this.errors.length === 0) {
        return true;
      } else {
        return false;
      }
    },
    validEmail(email) {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
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
