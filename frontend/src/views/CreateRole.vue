<template>
  <DashboardLayout>
    <div class="container-fluid">
      <h1>Create a role</h1>

      <ModalComponent type="Role" :isSuccess="isSuccess" />

      <!-- <div class="alert alert-danger" v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="(error, index) in errors" v-bind:key="index">
            {{ error }}
          </li>
        </ul>
      </div> -->

      <form @submit.prevent="createRole" method="POST">
        <FormComponent
          v-model="role_name.role_name"
          :label="role_name.label"
          type="text"
          :limit="role_name.limit"
          :errors="role_name.errors"
          :isSubmitted="isSubmitted"
        />
        <FormComponent
          v-model="role_description.role_description"
          :label="role_description.label"
          type="text"
          :limit="role_description.limit"
          :errors="role_description.errors"
          :isSubmitted="isSubmitted"
        />
        <button class="btn btn-secondary m-3" @click="resetForm" type="reset">
          Reset
        </button>
        <button class="btn btn-primary" type="submit" data-bs-toggle="modal" data-bs-target="#submitModal">
          Submit
        </button>
      </form>
    </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from "./Dashboard/Layout/DashboardLayout.vue";
import FormComponent from "../components/FormComponent.vue";
import ModalComponent from "../components/ModalComponent.vue";
import axios from "axios";

export default {
  name: "RoleView",
  components: {
    DashboardLayout,
    FormComponent,
    ModalComponent,
  },
  data() {
    return {
      role_name: {
        role_name: "",
        label: "Role Name",
        limit: "30",
        errors: ["Role already exists! Please try again"],
      },
      role_description: {
        role_description: "",
        label: "Role Description",
        limit: "170",
        errors: ["Role already exists! Please try again","Job Description exceeds character limit of 300! Please try again"],
      },
      isSuccess: false,
      isSubmitted: false
    };
  },
  methods: {
    createRole() {
      // === LINKING FRONT TO BACKEND ===
      // axios
      //   .post("http://localhost:3000/roles", {
      //     role_name: this.event.title,
      //     role_description: this.event.description,
      //   })
      //   .then((response) => {
      //     console.log(response);
      //   })
      //   .catch((error) => {
      //     this.errors = [];
      //     this.errors.push(error.data.message);
      //     console.log(error);
      //   });
      this.isSubmitted = true;

      // isSuccess is false if there are errors
    },
    resetForm() {
      this.role_name.role_name = "";
      this.role_description.role_description = "";
    },
  },
  mounted() {
    document.title = "LJMS - Create Roles";
    axios.get("https://api.kanye.rest/").then((response) => {
      console.log(response.data.quote);
    });
  },
};
</script>

<style scoped>
  
</style>
