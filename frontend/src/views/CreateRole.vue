<template>
  <DashboardLayout>
    <div class="container-fluid">
      <h1>Create a role</h1>
      <form @submit.prevent="createRole" method="POST">
        <FormComponent v-model="event.title" label="Role Name" type="text" limit="30" />
        <FormComponent v-model="event.description" label="Role Description" type="text" limit="170" />
        <button class="btn btn-secondary m-3" @click="resetForm" type="reset">Reset</button>
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
        title: "",
        description: "",
      },
      errors: [],
    };
  },
  methods: {
    createRole() {
      axios
        .post("http://localhost:3000/roles", {
            title: this.event.title,
            description: this.event.description,
        })
        .then((response) => {
            console.log(response);
        })
        .catch((error) => {
            this.errors = [];
            this.errors.push(error.data.m);
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
