<template>
  <DashboardLayout>
    <div class="container-fluid" id="skillMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="skills.length < 1 && noSkillFound==false" />
      
      <!-- Dashboard -->
      <div v-else class="">

        <!-- Search by Roles -->
        <div class="container-md my-5 mb-3 text-start">
          <PillSearchComponent 
            ctype="role" 
            @pillItems="getPill"
            func="filter"
          ></PillSearchComponent>
        </div>

        <!-- Create Skill -->
        <div class="row mt-3 mx-auto">
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <router-link to="/create-skill" tag="button" class="btn btn-dark btn-lg" v-if=" user.Role == 1">Create Skill</router-link>
          </div>
        </div>

        <!-- Skill Card -->
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
          <div 
            v-for="(value, key) in skills" v-bind:key="key" 
            v-show="this.pillItemsFromComponent.length == 0 || this.isFound(value.Roles)"
          >
            <card-component 
              :title="value.Skill_Name" 
              :desc="value.Skill_Description" 
              :active="value.Active" 
              :id="value.Skill_ID" 
              :pillList="value.Roles" 
              ctype="skill" 
              @reload="reload()"
            />
          </div>
        </div>
      </div>
      
      <!-- No Skill Found -->
      <div v-show="noSkillFound" class="fs-3 fw-bold text-center align-middle pt-5 my-5">
        Sorry! No skill found!
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
  import PillSearchComponent from "@/components/PillSearchComponent.vue";


  export default {
    name: "SkillView",
    components: {
      DashboardLayout,
      CardComponent,
      SpinnerComponent,
      PillSearchComponent,
  },
    data() {
      return {
        skills: [], // to get skills from database 
        numSkillsFound: 0,
        noSkillFound: false,
        pillItemsFromComponent: [],
        selectedRoles: [],
      }
    },
    methods: {
      reload() {
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/available";
        axios.get(url).then((response) => {
          var result = response.data.data
          this.skills = result
          if (this.skills.length == 0) {
            this.noSkillFound = true
          }
        });
      },

       getPill(item) {
        // emit content to be passed into the selectedList
        this.pillItemsFromComponent = item;
        this.selectedRoles = item.map(skill => {
          return skill.Role_Name
        });
        this.numSkillsFound = 0
      },

      isFound(arr1) {
        // show skills that include SOME of the roles selected
        // return (this.selectedRoles.some( x => arr1.includes(x) ));

        // show roles that include ALL of the skills selected
        if (this.selectedRoles.every( x => arr1.includes(x) )) {
          this.numSkillsFound += 1;
          if (this.noSkillFound) {
            this.noSkillFound = false;
          }
          return true;
        }
        if (this.numSkillsFound == 0) {
          this.noSkillFound = true;
        }
        return false;
      },
    },
    mounted() {
      document.title = "LJMS - Skills";
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

<style scoped>

#skillMain {
    min-height: 100vh;
  }
</style>