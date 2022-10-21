<template>
  <DashboardLayout>
    <div class="container-fluid" id="courseMain">
      <!-- Spinner -->
      <div v-if="courses.length < 1 && noCourseFound == false" id="rippleP">
        <div class="lds-ripple">
          <div></div>
          <div></div>
        </div>
      </div>
      <!-- <CourseComponent :title="" :desc="" :active="" :pillList="" :id=""></CourseComponent> -->

       <!-- Dashboard -->
       <div v-else class="">
      
          <div v-for="(value, key) in courses" v-bind:key="key">
             <CourseComponent :title="value.Course_Name" :desc="value.Course_Desc" :active="value.Course_Status" :pillList="value.Skills" :id="value.Course_ID" ctype="role"></CourseComponent>
        </div>
      </div>
      <!-- No Role Found -->
      <div v-show="noCourseFound" class="fs-3 fw-bold text-center align-middle pt-5 my-5">
        Sorry! No courses found!
      </div>
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
