<template>
  <DashboardLayout>
    <div class="container-fluid">
      <h1>Create a role</h1>
      <form @submit.prevent="createRole" method="POST">
        <FormComponent v-model="event.role_name" label="Role Name" type="text" limit="30" />
        <FormComponent v-model="event.role_description" label="Role Description" type="text" limit="170" />
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
        role_name: "",
        role_description: "",
      },
      errors: [],
    };
  },
  methods: {

  /// hi  
    createRole() {
      axios
        .post("http://localhost:3000/roles", {
            role_name: this.event.role_name,
            role_description: this.event.role_description,
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
        this.event.role_name = "";
        this.event.role_description = "";
    },
  },
  mounted() {
    document.title = "LJMS - Create Roles";
  },
};
</script>
