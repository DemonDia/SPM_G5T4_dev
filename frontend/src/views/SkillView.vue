<template>
  <DashboardLayout>
    <div class="container-fluid">
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
        <div v-for="(value, key) in skills" v-bind:key="key">
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
          title: "Beating Eggs",
          desc: "Masterchef level",
          active: true,
        },
        {
          title: "Rapping Nicki Minaj",
          desc: "No cap",
          active: true,
        },
        {
          title: "Opening soju bottle",
          desc: "With all the fluff and bartended skills",
          active: false,
        },
        {
          title: "Eating",
          desc: "Sample Description",
          active: true,
        },
        {
          title: "Eating",
          desc: "Sample Description",
          active: false,
        },
        {
          title: "Eating",
          desc: "Sample Description",
          active: false,
        },
      ],
      results: [] /* temporary array */,
      numSkills: 0 /* to populate based on length of array */,
    }
  },
  mounted() {
    document.title = "LJMS - Skills";
    axios.get("https://api.kanye.rest/").then((response) => {
      this.roles[1].desc = response.data.quote;
    });
  },
};
</script>

<style scoped>

</style>
