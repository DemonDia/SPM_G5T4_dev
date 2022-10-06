<template>
  <DashboardLayout>
    <div class="container-fluid">
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
        <div v-for="(value, key) in skills" v-bind:key="key">
          <card-component :title="value.SkillName" :desc="value.SkillDescription" :active="value.active"/>
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
      skills: /* to get roles from database */
      [
        {
          SkillName: "Beating Eggs",
          SkillDescription: "Masterchef level",
          active: true,
        },
        {
          SkillName: "Rapping Nicki Minaj",
          SkillDescription: "No cap",
          active: true,
        },
        {
          SkillName: "Eating",
          SkillDescription: "I think I do myself a disservice by comparing myself to Steve Jobs and Walt Disney and human beings that we've seen before. It should be more like Willy Wonka...and welcome to my chocolate factory. teve Jobs and Walt Disney and human beings that we've seen before. It should be more like Willy Wonka...and welcome to my chocolate factory.",
          active: true,
        },
      ],
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

</style>
