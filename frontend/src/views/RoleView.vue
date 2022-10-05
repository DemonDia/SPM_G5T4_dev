<template>
  <DashboardLayout>
    <div class="container-fluid">
      <div class="row mt-3">
        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
          <router-link to="/create-role" tag="button" class="btn btn-dark btn-lg">Create Role</router-link>
        </div>
      </div>
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
        <div v-for="(value, key) in roles" v-bind:key="key">
          <card-component :title="value.title" :desc="value.desc" :active="value.active" />
        </div>
      </div>
      </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from "./Dashboard/Layout/DashboardLayout.vue";
import CardComponent from "../components/CardComponent.vue";
import axios from "axios";

export default {
  name: "RoleView",
  components: {
    DashboardLayout,
    CardComponent,
  },
  data() {
    return {
      roles: /* to get roles from database */
      [
        {
          title: "Sous Chef - Egg Machine",
          desc: "Beat 30 eggs in 1 second",
          active: true,
        },
        {
          title: "Rapper",
          desc: "Sample Description",
          active: true,
        },
        {
          title: "Rapper",
          desc: "Sample Description",
          active: true,
        },
      ],
      results: [] /* temporary array */,
      numRoles: 0 /* to populate based on length of array */,
    }
  },
  mounted() {
    document.title = "LJMS - Roles";
    axios.get("https://api.kanye.rest/").then((response) => {
      this.roles[1].desc = response.data.quote;
    });
  },
};
</script>

<style scoped>

</style>
