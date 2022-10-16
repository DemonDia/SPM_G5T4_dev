<template>
  <DashboardLayout>
    <div class="container-fluid" id="roleMain">
      <!-- Spinner -->
      <div v-if="roles.length < 1 && noRoleFound==false" id="rippleP">
        <div class="lds-ripple">
          <div></div>
          <div></div>
        </div>
      </div>
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
  import DashboardLayout from "./Dashboard/Layout/DashboardLayout.vue";
  import CardComponent from "../components/CardComponent.vue";
  import axios from "axios";
  import { mapGetters } from "vuex";

  export default {
    name: "RoleView",
    components: {
      DashboardLayout,
      CardComponent,
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
      reload() {
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/available";
        axios.get(url).then((response) => {
          var result = response.data.data
          this.skills = result
          if (this.skills.length == 0) {
            this.noSkillFound = true
          }
        });
      },
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
    min-height: 100vh;
  }
  
  #rippleP {
    position: absolute;
    top: 45%;
    left: 47%;
  }

  .lds-ripple {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 80px;
  }
  .lds-ripple div {
    position: absolute;
    border: 4px solid rgb(0, 0, 0);
    opacity: 1;
    border-radius: 50%;
    animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
  }
  .lds-ripple div:nth-child(2) {
    animation-delay: -0.5s;
  }
  @keyframes lds-ripple {
    0% {
      top: 36px;
      left: 36px;
      width: 0;
      height: 0;
      opacity: 0;
    }
    4.9% {
      top: 36px;
      left: 36px;
      width: 0;
      height: 0;
      opacity: 0;
    }
    5% {
      top: 36px;
      left: 36px;
      width: 0;
      height: 0;
      opacity: 1;
    }
    100% {
      top: 0px;
      left: 0px;
      width: 72px;
      height: 72px;
      opacity: 0;
    }
  }
</style>
