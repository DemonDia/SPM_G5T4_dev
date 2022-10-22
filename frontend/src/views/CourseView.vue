<template>
  <DashboardLayout>
    <div class="container-fluid" id="courseMain" @reload="reload()">
      <!-- Spinner -->
      <div v-if="courses.length < 1 && noCourseFound == false" id="rippleP">
        <div class="lds-ripple">
          <div></div>
          <div></div>
        </div>
      </div>
       <!-- Dashboard -->
       <div v-else class="">
          <div v-for="(value, key) in courses" v-bind:key="key">
            <CourseComponent :course="value" :indx="key">
              {{addSkills(value.skills)}}
            </CourseComponent>
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
import DashboardLayout from "@/views/Dashboard/Layout/DashboardLayout.vue";
import CourseComponent from "@/components/CourseComponent.vue";
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "CourseView",
  components: {
    DashboardLayout,
    CourseComponent,
},
  data() {
    return {
      courses: [], // courses from database
      results: [], // temporary array
      numCourses: 0, // to populate based on length of array
      noCourseFound: false,
      selectedList: [],
      availSkills: ['Select skills:'],
      noSkillFound: false
    };
  },
  mounted() {
    document.title = "LJMS - Courses";
    var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/course/";
    axios.get(url).then((response) => {
      let result = response.data.data;
      this.courses = result;
      this.courses.length == 0 ? (this.noCourseFound = true) : null;
    });
    this.getSkills();
  },
  computed: {
    ...mapGetters({
      user: "auth/user",
      authenticated: "auth/authenticated",
    }),
  },
  methods: {
    reload() {
      this.selectedList = []
    },
  }
};
</script>

<style scoped>
#courseMain {
  min-height: 100vh;
}

#rippleP {
  position: absolute;
  top: 45%;
  left: 47%;
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
