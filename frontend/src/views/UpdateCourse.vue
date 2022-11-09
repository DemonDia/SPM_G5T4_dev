<template>
  <DashboardLayout>
    <div class="container-fluid p-sm-5" id="updateCourseMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="!noCourseFound" />

      <!-- Content -->
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

        <!-- Form -->
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
            func="search"
          ></PillSearchComponent>
        </form>

        <!-- Button -->
        <div class="row d-flex justify-content-around my-sm-3 my-md-5 p-3">
          <button
            type="button"
            class="btn col-md-4 col-sm-5 m-2"
            @click="handleSubmit"
            data-bs-toggle="modal"
            data-bs-target="#submitModal"
            id="submitBtn"
          >
            Update Course
          </button>
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from "@/views/Dashboard/Layout/DashboardLayout.vue";
import FormComponent from "@/components/FormComponent.vue";
import ModalComponent from "@/components/ModalComponent.vue";
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
    document.title = "LJMS - Update Course";
    // get course information from backend
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
  #updateCourseMain {
    min-height: 100vh;
  }
  .back-btn {
    border: none;
    background: none;
    line-height: 1;
    font-weight: 500;
    color: #434ce8;
    font-size: 18px;
  }

  .back-btn:hover {
    color: #404089;
    transition: 0.2s ease-in-out;
  }

  #submitBtn {
    background-color: #434ce8;
    color: #fbfbfb;
    border: none;
  }

  #submitBtn:hover {
    background-color: #404089;
    transition: 0.2s ease-in-out;
  }
</style>
