<template>
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
      <div class="preview" v-show="visibleContent" v-html="markdownText"></div>
      <textarea
        v-show="!visibleContent"
        v-model="content"
        class="input-form"
        placeholder="Content"
      ></textarea>
    </div>
    <div class="field-area file-selector">
      <input id="postImageFile" type="file" @change="onFileChange($event)" />
      <label for="postImageFile">Main image: {{ fileName }}</label>
    </div>
    <div class="button">
      <button class="btn" type="button" @click="submit()">Submit</button>
    </div>
  </form>
</template>

<script>
import marked from "marked";

import BackendServices from "@/services/BackendServices.js";

export default {
  props: {
    edit: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      visibleContent: false,
      title: "",
      description: "",
      content: "",
      image: null,
      fileName: "Choose File",
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
      if (!this.edit) {
        BackendServices.addPost(data, this.image)
          .then((response) => {
            console.log(response.data);
            this.$router.push(`http://localhost:8080/post/${response.data.id}`);
          })
          .catch((response) => {
            console.err(response.error);
          });
      } else {
        BackendServices.editPost(data, this.$route.params.id, this.image)
          .then((response) => {
            console.log(response.data);
            this.$router.push({
              name: "Post",
              params: { id: this.$route.params.id },
            });
            // this.$router.push(`${this.$route.params.id}`);
          })
          .catch((response) => {
            console.err(response.error.data);
          });
      }
    },
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.image = files[0];
      this.fileName = this.image.name;
    },
  },
  created() {
    if (this.edit) {
      BackendServices.getPost(this.$route.params.id)
        .then((response) => {
          this.title = response.data.title;
          this.description = response.data.description;
          this.content = response.data.content;
          // BackendServices.getImage(response.data.image)
          //   .then((response) => response.blob())
          //   .then((blobResponse) => {
          //     const blob = blobResponse;
          //     blob.lastModifiedDate = new Date();
          //     blob.name = "archivo";
          //     this.image = blob;
          //   });
        })
        .catch((response) => console.err(response.error));
    }
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

.preview {
  width: 100%;
}
</style>
