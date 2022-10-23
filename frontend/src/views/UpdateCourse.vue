<template>
  <DashboardLayout>
    <div class="container-fluid p-sm-5" id="updatecourseMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="!noCourseFound" />
      <div
        v-else
        class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body"
      >
        <button @click="goBack" class="ph-arrow-left back-btn mb-3">
          Back
        </button>
        <h3>Update a Course</h3>
        <h6 class="text-secondary mt-3 mb-3">
          Update skills of a course to make it more relevant to the current
        </h6>

        <!-- Popup -->
        <div v-show="checked">
          <ModalComponent
            type="Course"
            func="update"
            :isSuccess="isSuccess"
            @clicked="onClickModal"
          />
        </div>

        <!-- Content -->
        <form @submit.prevent="handleSubmit" method="POST">
          <FormComponent
            v-model="course_name.course_name"
            :label="course_name.label"
            type="text"
            :limit="course_name.limit"
            :errors="course_name.errors"
            :isSubmitted="isSubmitted"
            :formType="course_name.formType"
            :disabled="1"
          />

          <FormComponent
            v-model="course_description.course_description"
            :label="course_description.label"
            type="text"
            :limit="course_description.limit"
            :errors="course_description.errors"
            :isSubmitted="isSubmitted"
            :formType="course_description.formType"
            :disabled="1"
          />

          <PillSearchComponent
            class="mt-3"
            ctype="skill"
            :skills="skills_array"
            @pillItems="getPill"
          ></PillSearchComponent>
        </form>

        <!-- Buttons -->
        <div class="row d-flex justify-content-around my-sm-3 my-md-5 p-3">
          <button
            type="button"
            class="btn col-md-4 col-sm-5 m-2 btn-primary"
            @click="handleSubmit"
            data-bs-toggle="modal"
            data-bs-target="#submitModal"
          >
            Update Course
          </button>
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from "./Dashboard/Layout/DashboardLayout.vue";
import FormComponent from "../components/FormComponent.vue";
import ModalComponent from "../components/ModalComponent.vue";
import axios from "axios";
import PillSearchComponent from "@/components/PillSearchComponent.vue";
import PillComponent from "@/components/PillComponent.vue";
import SpinnerComponent from "@/components/SpinnerComponent.vue";

export default {
  name: "UpdateCourse",
  components: {
    DashboardLayout,
    FormComponent,
    ModalComponent,
    PillSearchComponent,
    PillComponent,
    SpinnerComponent,
  },
  data() {
    return {
      course_name: {
        course_name: "",
        label: "Course Name",
        limit: "30",
        errors: [],
        formType: "input",
      },
      course_description: {
        course_description: "",
        label: "Course Description",
        limit: "170",
        errors: [],
        formType: "textarea",
      },
      isSuccess: false,
      isSubmitted: false,
      checked: false,
      pillItemsFromComponent: [],
      noCourseFound: false,
      skills_array: [],
      currentCourse_ID: this.$route.params.course_id,
    };
  },
  methods: {
    handleSubmit() {
      // submitted form
      this.isSubmitted = true;
      // check success
        this.assignSkills(this.currentCourse_ID).then((result) => {
          this.resetErrors();
          // this.resetForm();
          this.isSuccess = true;
          this.checked = true; // show Modal
        });
    },

    assignSkills(course_id) {
      var assignSkillsUrl =
        "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/courseskillrelations/" +
        course_id;
      return new Promise((resolve, reject) => {
        axios
          .put(assignSkillsUrl, {
            Skills: this.pillSkill_IDArray,
          })
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

    getCourseInfo(course_id) {
      var getcourseUrl =
        "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/course/" +
        course_id;
      return new Promise((resolve, reject) => {
        axios
          .get(getcourseUrl)
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

    onClickModal(value) {
      // modal is closed
      // reset checked value:
      this.checked = value;
      if (this.isSuccess) {
        // go back to View All
        this.$router.replace({ name: "courses" });
      }
    },

    getPill(item) {
      // emit content to be passed into the pillItemsFromComponent
      this.pillItemsFromComponent = item;
    },

    resetErrors() {
      // reset fields
      this.course_name.errors = [];
      this.course_description.errors = [];
      this.isSubmitted = NaN;
      this.checked = NaN;
      this.isSuccess = NaN;
    },
  },
  computed: {
    // This computed function will enumerate the pillItemsFromComponent where the key/value items is stored
    // And then it will return the value of the key "skill_name" to be displayed in the pill
    pillValue() {
      const pillItems = [];
      this.pillItemsFromComponent.forEach((value) => {
        pillItems.push(value.Skill_Name);
      });
      return pillItems;
    },
    // This computed function will enumerate the pillItemsFromComponent where the key/value items is stored
    // And then it will return the value of the key "skill_id" and return to the assign skill function.
    pillSkill_IDArray() {
      const pillItems = [];
      this.pillItemsFromComponent.forEach((value) => {
        pillItems.push(value.Skill_ID);
      });
      return pillItems;
    },
    goBack() {
      this.$router.replace({ name: "courses" });
    },
  },
  async mounted() {
    document.title = "LJMS - Update course";
    // get course information from backend
    console.log(this.currentCourse_ID);
    var courseInfo = await this.getCourseInfo(this.currentCourse_ID);
    courseInfo
      ? (this.noCourseFound = true)
      : (this.noCourseFound = false);

    // load data into the v-model and array
    this.course_name.course_name = courseInfo.data.data.Course_Name;
    this.course_description.course_description =
      courseInfo.data.data.Course_Desc;
    this.skills_array = courseInfo.data.data.Skills;
    this.pillItemsFromComponent =  courseInfo.data.data.Skills;
  },
};
</script>

<style scoped>
.back-btn {
  border: none;
  background: none;
  line-height: 1;
  font-weight: 500;
  color: #113f7c;
  font-size: 18px;
}

.back-btn:hover {
  color: #1a73e8;
  transition: 0.3s ease-in-out;
}

#updatecourseMain {
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
