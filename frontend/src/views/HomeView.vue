<template>
  <DashboardLayout>
    <div class="home">
      <SearchComponent></SearchComponent>
      <img alt="Vue logo" src="../assets/logo.png" />
      <HelloWorld msg="Welcome to Your Vue.js App" />
    </div>
  </DashboardLayout>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import DashboardLayout from "@/views/Dashboard/Layout/DashboardLayout.vue";
import SearchComponent from "@/components/SearchComponent.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
    DashboardLayout,
    SearchComponent
  },
  mounted() {
   document.title = "LJMS - Home";
  },
};
</script>
