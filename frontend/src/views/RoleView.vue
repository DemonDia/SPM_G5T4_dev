<template>
  <DashboardLayout>
    <div class="container-fluid" id="roleMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="roles.length < 1 && noRoleFound==false" />

      <!-- Dashboard -->
      <div v-else class="">

        <!-- Search by Skills -->
        <div class="container-md my-5 mb-3 text-start">
          <PillSearchComponent ctype="skill" @pillItems="getPill"></PillSearchComponent>
        </div>

        <!-- Create Role -->
        <div class="row mt-3 mx-auto">
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <router-link to="/create-role" tag="button" class="btn btn-dark btn-lg mx-3" v-if=" user.Role == 1">Create Role</router-link>
          </div>
        </div>

        <!-- Role Card -->
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 mx-3">
          <div 
            v-for="(value, key) in roles" v-bind:key="key" 
            v-show="this.pillItemsFromComponent.length == 0 || this.isFound(value.Skills)"
          >
            <card-component 
              :title="value.Role_Name" 
              :desc="value.Role_Description" 
              :active="value.Active" 
              :pillList="value.Skills" 
              :id="value.Role_ID" 
              ctype="role" 
              @reload="reload()"
              
            />
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
  import PillSearchComponent from '@/components/PillSearchComponent.vue'

  export default {
    name: "RoleView",
    components: {
    DashboardLayout,
    CardComponent,
    SpinnerComponent,
    PillSearchComponent
},
    data() {
      return {
        roles: [], // roles from database
        numRolesFound: 0,
        noRoleFound: false,
        availSkills: ['Select skills:'],
        noSkillFound: false,
        pillItemsFromComponent: [],
        selectedSkills: [],
        filteredRoles: [],
      }
    },
    methods: {
      async reload() {
        this.pillItemsFromComponent = [];
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
      },

      getPill(item) {
        // emit content to be passed into the selectedList
        this.pillItemsFromComponent = item;
        this.selectedSkills = item.map(role => {
          return role.Skill_Name
        });
        this.numRolesFound = 0
      },

      isFound(arr1) {
        console.log(arr1)
        // show roles that include SOME of the skills selected
        // return (this.selectedSkills.some( x => arr1.includes(x) ));

        // show roles that include ALL of the skills selected
        if (this.selectedSkills.every( x => arr1.includes(x) )) {
          this.numRolesFound += 1;
          if (this.noRoleFound) {
            this.noRoleFound = false;
          }
          return true;
        }
        if (this.numRolesFound == 0) {
          this.noRoleFound = true;
        }
        return false;
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
    min-height:  100vh;
  }
</style>
