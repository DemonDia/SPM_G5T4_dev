<template>
  <DashboardLayout>
    <div class="container-fluid">
      <h1>Create a role</h1>

      <div class="alert alert-danger" v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="(error, index) in errors" v-bind:key="index">
            {{ error }}
          </li>
        </ul>
      </div>

      <form @submit.prevent="createRole" method="POST">
        <FormComponent
          v-model="event.role_name"
          label="Role Name"
          type="text"
          limit="30"
        />
        <FormComponent
          v-model="event.role_description"
          label="Role Description"
          type="text"
          limit="170"
        />
        <button class="btn btn-secondary m-3" @click="resetForm" type="reset">
          Reset
        </button>
        <button class="btn btn-primary" type="submit">Submit</button>
      </form>
    </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from "./Dashboard/Layout/DashboardLayout.vue";
import FormComponent from "../components/FormComponent.vue";
import axios from "axios";

export default {
  name: "RoleView",
  components: {
    DashboardLayout,
    FormComponent,
  },
  data() {
    return {
      event: {
        role_name: "",
        role_description: "",
      },
      errors: ["Role already exists! Please try again","Job Description exceeds character limit of 300! Please try again"],
    };
  },
  methods: {
    createRole() {
      axios
        .post("http://localhost:3000/roles", {
          role_name: this.event.title,
          role_description: this.event.description,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          this.errors = [];
          this.errors.push(error.data.message);
          console.log(error);
        });
    },
    resetForm() {
      this.event.title = "";
      this.event.description = "";
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
