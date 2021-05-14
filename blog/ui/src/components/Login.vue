<template>
  <!-- <div class="modal-content"> -->
  <!-- <div class="modal-header">
      <span> </span>
      <h2>Login</h2>
      <span> </span>
      <span class="close" @click="hideModal()">&times;</span>
    </div> -->
  <div class="modal-body">
    <form class="form">
      <div class="field-area">
        <input type="email" class="input-form" placeholder="Email" />
      </div>
      <div class="field-area">
        <input type="password" class="input-form" placeholder="Password" />
      </div>
    </form>
  </div>
  <div class="modal-footer">
    <button type="button" class="btn">Submit</button>
    <div class="forgot-password">
      <a href="#">Forgot Password?</a>
    </div>
  </div>
  <!-- </div<div class="modal-content">> -->
</template>

<script>
export default {};
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
