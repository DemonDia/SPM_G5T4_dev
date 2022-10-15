<template>
  <DashboardLayout>
    <div class="container-fluid" id="skillMain">
      <!-- Spinner -->
      <div v-if="skills.length < 1 && noSkillFound==false" id="rippleP">
        <div class="lds-ripple">
          <div></div>
          <div></div>
        </div>
      </div>
      <!-- Dashboard -->
      <div v-else class="">
        <div class="row mt-3 mx-auto">
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <router-link to="/create-skill" tag="button" class="btn btn-dark btn-lg" v-if=" user.Role == 1">Create Skill</router-link>
          </div>
        </div>
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
          <div v-for="(value, key) in skills" v-bind:key="key">
            <card-component :title="value.Skill_Name" :desc="value.Skill_Description" :active="value.Active" :id="value.Skill_ID" ctype="skill" @reload="reload()"/>
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
import DashboardLayout from "./Dashboard/Layout/DashboardLayout.vue";
import CardComponent from "../components/CardComponent.vue";
import axios from "axios";
import { mapGetters } from "vuex";


export default {
  name: "SkillView",
  components: {
    DashboardLayout,
    CardComponent,
  },
  data() {
    return {
      skills: /* to get skills from database */
      [],
      results: [], // temporary array
      numSkills: 0, // to populate based on length of array
      noSkillFound: false,
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
    }
  },
  async mounted() {
    document.title = "LJMS - Skills";
      var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/available";
      await axios.get(url).then((response) => {
        var result = response.data.data
        this.skills = result
        if (this.skills.length == 0) {
          this.noSkillFound = true
        }
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

#skillMain {
    min-height: 100vh;
  }

</style>
