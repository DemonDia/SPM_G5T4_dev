<template>
  <DashboardLayout>
    <div class="container-fluid">
      <h1>Create a role</h1>
      <form>
        <FormComponent v-model="event.title" label="Role Name" type="text" />

        <FormComponent
          v-model="event.description"
          label="Role Description"
          type="text"
        />

        <button class="btn btn-secondary m-3" type="reset">Reset</button>
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
    };
  },
  mounted() {
    document.title = "LJMS - Create Roles";
    axios.get("https://api.kanye.rest/").then((response) => {
      console.log(response.data.quote);
    });
  },
};
</script>
