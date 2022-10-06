<template>
  <DashboardLayout>
    <div class="container-fluid" id="skillMain">
      <!-- Spinner -->
      <div v-if="skills.length < 1" id="rippleP">
        <div class="lds-ripple">
          <div></div>
          <div></div>
        </div>
      </div>
      <!-- Dashboard -->
      <div v-else class="">
        <div class="row mt-3 mx-auto">
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <router-link to="/create-skill" tag="button" class="btn btn-dark btn-lg">Create Skill</router-link>
          </div>
        </div>
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
          <div v-for="(value, key) in skills" v-bind:key="key">
            <card-component :title="value.SkillName" :desc="value.SkillDescription" :active="value.active" />
          </div>
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
    }
  },
  mounted() {
    document.title = "LJMS - Skills";
    var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/";
      axios.get(url).then((response) => {
        var result = response.data.data
        this.skills = result
      });
  },
};
</script>

<style scoped>

#skillMain {
    min-height: 100vh;
  }

  #rippleP {
    position: absolute;
    top: 45%;
    left: 50%;
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
