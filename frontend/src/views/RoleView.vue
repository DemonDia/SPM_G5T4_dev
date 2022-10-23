<template>
  <DashboardLayout>
    <div class="container-fluid" id="roleMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="roles.length < 1 && noRoleFound==false" />

      <!-- Dashboard -->
      <div v-else class="">
        <div class="row mt-3 mx-auto">
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <router-link to="/create-role" tag="button" class="btn btn-dark btn-lg" v-if=" user.Role == 1">Create Role</router-link>
          </div>
        </div>
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
          <div v-for="(value, key) in roles" v-bind:key="key">
            <card-component :title="value.Role_Name" :desc="value.Role_Description" :active="value.Active" :pillList="value.Skills" :id="value.Role_ID" ctype="role" @reload="reload()"/>
          </div>
        </div>
      </div>

      <!-- No Role Found -->
      <div v-show="noRoleFound" class="fs-3 fw-bold text-center align-middle pt-5 my-5">
        Sorry! No role found!
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
  import DashboardLayout from "@/views/Dashboard/Layout/DashboardLayout.vue";
  import CardComponent from "@/components/CardComponent.vue";
  import axios from "axios";
  import { mapGetters } from "vuex";
  import SpinnerComponent from "@/components/SpinnerComponent.vue";

  export default {
    name: "RoleView",
    components: {
    DashboardLayout,
    CardComponent,
    SpinnerComponent
},
    data() {
      return {
        roles: [], // roles from database
        results: [], // temporary array
        numRoles: 0, // to populate based on length of array
        noRoleFound: false,
      }
    },
    methods: {
     async reload() {
      var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/available";
      await axios.get(url).then((response) => {
        var result = response.data.data
        this.roles = result
        if (this.roles.length == 0) {
          this.noRoleFound = true
        }
      }).catch((error) => {
        console.log(error)
      });
    }
    },
    mounted() {
      document.title = "LJMS - Roles";
      this.reload()
    },
    computed: {
      ...mapGetters({
        user: "auth/user",
        authenticated: "auth/authenticated",
      }),
    },
  };
</script>

<style>
  #roleMain {
    min-height:  100vh;
  }
</style>
