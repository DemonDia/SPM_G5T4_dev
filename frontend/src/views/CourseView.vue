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
          <!-- Search by Skills -->
          <div class="container-sm my-5 mb-3 text-start">
            <PillSearchComponent ctype="skill" @pillItems="getPill"></PillSearchComponent>
          </div>
          <!-- Course Card -->
          <div v-for="(value, key) in courses" v-bind:key="key">
            <CourseComponent 
              :course="value" 
              :indx="key" 
              v-if="this.pillItemsFromComponent.length == 0 || this.isFound(value.Skills)">
            </CourseComponent>
        </div>
      </div>
      <!-- No Course Found -->
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
import PillSearchComponent from '@/components/PillSearchComponent.vue'

export default {
  name: "CourseView",
  components: {
    DashboardLayout,
    CourseComponent,
    PillSearchComponent
},
  data() {
    return {
      courses: [], // courses from database
      numCoursesFound: 0, 
      noCourseFound: false,
      availSkills: ['Select skills:'],
      noSkillFound: false,
      pillItemsFromComponent: [],
      selectedSkills: [],
    };
  },
  methods: {
    getPill(item) {
      // emit content to be passed into the selectedList
      this.pillItemsFromComponent = item;
      this.selectedSkills = item.map(course => {
        return course.Skill_Name
      });
      this.numCoursesFound = 0
    },

    reload() {
      this.pillItemsFromComponent = [];
    },

    isFound(arr1) {
      // show courses that include SOME of the skills selected
      // return (this.selectedSkills.some( x => arr1.includes(x) ));

      // show courses that include ALL of the skills selected
      if (this.selectedSkills.every( x => arr1.includes(x) )) {
        this.numCoursesFound += 1;
        if (this.noCourseFound) {
          this.noCourseFound = false;
        }
        return true;
      }
      if (this.numCoursesFound == 0) {
        this.noCourseFound = true;
      }
      return false;
    },
  },
  mounted() {
    document.title = "LJMS - Courses";
    var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/course/";
    axios.get(url).then((response) => {
      let result = response.data.data;
      this.courses = result;
      this.courses.length == 0 ? (this.noCourseFound = true) : null;
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
