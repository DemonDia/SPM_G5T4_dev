<template>
  <DashboardLayout>
    <div class="container-fluid" id="LJMain" @reload="reload()">
      <!-- Spinner -->
      <SpinnerComponent v-if="LJ.length < 1 && noLJFound == false" />

      <!-- Dashboard -->
      <div v-else>

         <!-- Create Role -->
         <div class="row mt-3 mx-auto">
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <router-link to="/create-journey" tag="button" class="btn btn-dark btn-lg mx-3">Create Learning Journey</router-link>
          </div>
        </div>

        <!-- Course Card -->
        <div v-for="(value, key) in LJ" v-bind:key="key">
          <LongCardComponent 
            :cardValue="value" 
            :indx="key" 
            v-if="value.Courses.length > 0">
          </LongCardComponent>
        </div>
      </div>

      <!-- No Course Found -->
      <div v-show="noLJFound" class="fs-3 fw-bold text-center align-middle pt-5 my-5">
        Sorry! No Learning Journey found!
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
  // @ is an alias to /src
  import DashboardLayout from "@/views/Dashboard/Layout/DashboardLayout.vue";
  import LongCardComponent from "@/components/LongCardComponent.vue";
  import axios from "axios";
  import { mapGetters } from "vuex";
  import PillSearchComponent from '@/components/PillSearchComponent.vue'
  import SpinnerComponent from "@/components/SpinnerComponent.vue";

  export default {
    name: "LJView",
    components: {
      DashboardLayout,
      LongCardComponent,
      PillSearchComponent,
      SpinnerComponent
  },
    data() {
      return {
        LJ: [], // courses from database
        numLJFound: 0, 
        noLJFound: false,
      };
    },
    methods: {},
    mounted() {
      document.title = "LJMS - Learning Journey";
      var getLJ = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/learningjourney/staff/" + this.user.StaffID;
    
      axios.get(getLJ).then((response) => {
        let result = response.data.data;
        this.LJ = result;
        this.LJ.length == 0 ? (this.noLJFound = true) : null;
      });
      
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
  #LJMain {
    min-height: 100vh;
  }
</style>
