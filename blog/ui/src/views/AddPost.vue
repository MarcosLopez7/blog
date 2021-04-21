<template>
  <div class="title">
    <h1>Create Post</h1>
    <form class="form">
      <div class="field-area">
        <input
          v-model="title"
          class="input-form"
          type="text"
          placeholder="Title"
        />
      </div>
      <div class="field-area">
        <textarea
          v-model="description"
          class="input-form"
          placeholder="Description"
        ></textarea>
      </div>
      <div class="field-area">
        <button
          type="button"
          class="btn visible-button"
          @click="visibleContent = !visibleContent"
        >
          <i class="fa fa-eye" aria-hidden="true"></i>
        </button>
        <div
          class="preview"
          v-show="visibleContent"
          v-html="markdownText"
        ></div>
        <textarea
          v-show="!visibleContent"
          v-model="content"
          class="input-form"
          placeholder="Content"
        ></textarea>
      </div>
      <div class="field-area file-selector">
        <input id="postImageFile" type="file" @change="onFileChange($event)" />
        <label for="postImageFile">Main image: Choose File</label>
      </div>
      <div class="button">
        <button class="btn" type="button" @click="submit()">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import marked from "marked";

import BackendServices from "@/services/BackendServices.js";

export default {
  data() {
    return {
      visibleContent: false,
      title: "",
      description: "",
      content: "",
      image: null,
    };
  },
  computed: {
    markdownText() {
      return marked(this.content, { sanitize: true });
    },
  },
  methods: {
    submit() {
      const data = {
        title: this.title,
        description: this.description,
        content: this.markdownText,
      };

      BackendServices.addPost(data, this.image)
        .then((response) => {
          console.log(response.data);
          this.$router.push(`http://localhost:8080/post/${response.data.id}`);
        })
        .catch((response) => {
          console.err(response.error);
        });
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.image = files[0];
    },
  },
};
</script>

<style scoped>
.field-area {
  margin: 25px 0;
  max-width: 800px;
  width: 100%;
}

.input-form {
  width: 100%;
  font-size: 1.3rem;
  border-radius: 5px;
  border-color: var(--bg-card);
  border-width: 2px;
}

.field-area input {
  height: 30px;
}

.field-area textarea {
  height: 100px;
}

.form {
  align-items: center;
  display: flex;
  flex-flow: column wrap;
  background-color: rgba(153, 153, 153, 0.5);
  max-width: 850px;
  width: 100%;
  margin: 0 auto;
  border-radius: 5px;
  padding: 20px 10px;
}

h1 {
  font-size: 2.5rem;
  font-weight: 550;
  padding: 15px 0;
}

.file-selector {
  display: flex;
  flex-flow: flex wrap;
}

.file-selector label {
  width: 100%;
  margin: 0 auto;
  font-size: 1.2rem;
  border: 1px solid var(--bg-card);
  background-color: #ced4da;
  background-clip: padding-box;
  border-radius: 5px;
  /* height: 30px; */
  padding: 5px 20px;
  color: #000;
  max-width: 300px;
}

.file-selector input {
  cursor: pointer;
  /* border: 1px solid #ced4da;
  background-color: #fff; */
  background-clip: padding-box;
  height: 30px;
  display: none;
}

.form button {
  background-color: var(--bg-card);
}

.visible-button {
  float: right;
  margin: 5px 0;
}

.form button:hover {
  color: #fff;
  background-color: #0b5ed7;
  border-color: #0a58ca;
}

.btn {
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  color: #fff;
  text-align: center;
  text-decoration: none;
  vertical-align: middle;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  background-color: transparent;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.preview {
  width: 100%;
}
</style>
