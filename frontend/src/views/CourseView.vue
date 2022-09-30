<template>
  <DashboardLayout>
    <div class="home">
      <img alt="Vue logo" src="../assets/logo.png" />
      <HelloWorld msg="Welcome to Your Vue.js App" />
    </div>
  </DashboardLayout>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import DashboardLayout from "@/views/Dashboard/Layout/DashboardLayout.vue";

export default {
  name: "CourseView",
  components: {
    HelloWorld,
    DashboardLayout,
  },
  mounted() {
   document.title = "LJMS - Courses";
  },
};
</script>
