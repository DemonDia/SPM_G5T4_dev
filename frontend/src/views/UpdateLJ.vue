<template>
  <DashboardLayout>
    <div class="container-fluid p-sm-5" id="updateLJMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="!noLJFound" />

      <!-- Content -->
      <div
        v-else
        class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body"
      >
        <button @click="goBack" class="ph-arrow-left back-btn mb-3">
          Back
        </button>
        <h3>Update a Learning Journey</h3>
        <h6 class="text-secondary mt-3 mb-3">
          Add or remove courses to this learning journey
        </h6>

        <!-- Popup -->
        <div 
          v-show="addCourseActive"
          id="addCourseModal"
          class="modal fade" 
          tabindex="-1" 
          aria-labelledby="addCourseModalLabel" 
          aria-hidden="true" 
        >
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="addCourseModalLabel"> {{addCourseModalContent[1].modalTitle}} </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                {{addCourseModalContent[1].modalDesc}}
              </div>
              <div class="modal-footer">
                <button 
                  class="btn" 
                  data-bs-target="#addCourseModal2" 
                  data-bs-toggle="modal" 
                  data-bs-dismiss="modal"
                  id="nextBtnModal"
                >
                  {{modalBtnText}}
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="modal fade" id="addCourseModal2" aria-hidden="true" aria-labelledby="addCourseModalLabel2" tabindex="-1">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="addCourseModalLabel2"> {{addCourseModalContent[2].modalTitle}} </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                {{addCourseModalContent[2].modalDesc}}
              </div>
              <div class="modal-footer">
                <button 
                  class="btn" 
                  id="backBtnModal"
                  data-bs-target="#addCourseModal" 
                  data-bs-toggle="modal" 
                  data-bs-dismiss="modal"
                >
                  Back to first
                </button>
                <button 
                  class="btn" 
                  id="submitBtnModal"
                  data-bs-target="#addCourseModal" 
                  data-bs-toggle="modal" 
                  data-bs-dismiss="modal"
                >
                  Submit
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Spinner -->
        <SpinnerComponent v-if="!noLJFound"/>

        <div v-else>
          <!-- Role Details -->
          <div id="roleDetails" class="shadow p-3 mb-5 rounded">
            <p class="fs-5 fw-bold my-0">
              Your Goal
            </p>
            <table class="table p-1">
              <tr class="row">
                <th class="col-sm-6 col-md-3">
                  <p class="m-0 pb-0">Selected Role</p>
                </th>
                <td class="col">
                  <p class="m-1 my-0 p-1 fw-bold">{{this.role.role_name}}</p>
                  <p class="m-1 my-0 p-1 fst-italic">{{this.role.role_description}}</p>
                </td>
              </tr>
              <tr class="row">
                <th class="col-sm-6 col-md-3">
                  <p class="m-0 pb-0">Selected Skills</p>
                </th>
                <td class="col">
                  <p class="m-1 my-0 p-1 fw-bold">CHANGE THIS SKILL NAME</p>
                  <p class="m-1 my-0 p-1 fst-italic">CHANGE THIS SKILL DESC</p>
                </td>
              </tr>
            </table>
          </div>

          <!-- Courses -->
          <div id="courseDetails" class="mb-5 rounded text-center">
            <p class="fs-5 fw-bold my-1 text-start">
              Your Courses
            </p>
            <!-- Add a new course -->
            <button 
              type="button" 
              class="btn" 
              id="addBtn" 
              @click="addCourse()" 
              data-bs-toggle="modal" 
              data-bs-target="#addCourseModal"
              @mouseover="hoverText='+ Add a new course'" 
              @mouseleave="hoverText='+'"
            >
              {{hoverText}}
            </button>
            <!-- See existing courses -->
            <div v-for="(value, key) in courses" v-bind:key="key" class="card-component row mx-1 my-3">
              <div class="flex-grow-1 card-content p-1 px-4 my-1 col-sm-12 col-md-7">
                <div class="tags text-start p-2 ps-0 my-0">
                  <span class="badge text-dark me-2" id="typeBadge">
                    <p class="m-0">{{ getCourseInfo(value.Course_ID, "type") }}</p>
                  </span>
                  <span class="badge text-dark me-2" id="catBadge">
                    <p class="m-0">{{ getCourseInfo(value.Course_ID, "cat") }}</p>
                  </span>
                </div>
                <h5 class="card-title text-start my-1">
                  {{ value.Course_Name }}
                </h5>
                <div class="card-body mb-2">
                  <p class="card-text text-start">{{ getCourseInfo(value.Course_ID, "desc") }}</p>
                </div>
              </div>
              <div class="col-auto p-4 pt-0 m-sm-0 m-md-2 pt-md-2 pe-md-2">
                <button type="button" class="btn mx-auto" id="removeBtn" @click="removeCourse()">
                  Remove
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from "@/views/Dashboard/Layout/DashboardLayout.vue";
import FormComponent from "@/components/FormComponent.vue";
import axios from "axios";
import SpinnerComponent from "@/components/SpinnerComponent.vue";

export default {
  name: "UpdateLJ",
  components: {
    DashboardLayout,
    FormComponent,
    SpinnerComponent,
  },
  data() {
    return {
      role: {
        role_id: 0,
        role_name: "",
        role_description: "",
      },
      courses: [],
      skills: [],
      allCourses: [],
      isSuccess: false,
      isSubmitted: false,
      noLJFound: false,
      noCourseFound: false,
      noSkillFound: false,
      currentLJ_ID: this.$route.params.lj_id,
      addCourseActive: false,
      addCourseModalContent: {
        1: {
          modalTitle: "Change skills (optional)",
          modalDesc: "You may change the skills selected for this learning journey"
        },
        2: {
          modalTitle: "Select new courses",
          modalDesc: "Select courses you wish to add to this learning journey"
        }
      },
      hoverText: '+',
      modalPg: 1,
      modalBtnText: "Next: Select Courses",
    };
  },
  methods: {
    getLJInfo(lj_id) {
      var getLJUrl =
        "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/learningjourney/" + lj_id;
      return new Promise((resolve, reject) => {
        axios
          .get(getLJUrl)
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

    getRoleInfo(role_id) {
      var getRoleUrl =
        "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/" +
        role_id;
      return new Promise((resolve, reject) => {
        axios
          .get(getRoleUrl)
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

    getSkillInfo(skill_id) {
      var getSkillUrl = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roleskillrelations/" + 1;
      return new Promise((resolve, reject) => {
        axios
          .get(getSkillUrl)
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

    getCourses() {
      var getCoursesUrl = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/course/"
      return new Promise((resolve, reject) => {
        axios
          .get(getCoursesUrl)
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

    getCourseInfo(id, resultType) {
      let course = this.allCourses.filter(function(course) {return course.Course_ID==id})[0];
      if (resultType == "type") {
        return course.Course_Type
      } else if (resultType == "cat") {
        return course.Course_Category
      } else {
        return course.Course_Desc
      }
    },

    onClickModal() {
      // modal is closed
      // reset modal page number
      this.modalPg = 1;
      if (this.isSuccess) {
        // go back to View All
        this.$router.replace({ name: "learningjourney" });
      }
      console.log(this.modalPg)
    },

    resetErrors() {
      // reset fields
      this.isSubmitted = NaN;
      this.isSuccess = NaN;
    },

    addCourse() {
      this.addCourseActive = true;
      this.modalPg = 1;
      console.log(this.modalPg)
    },

    nextModalPg() {
      this.modalPg += 1;
      if (this.modalPg == 2) {
        this.modalBtnText = "Submit";
      } else {
        this.modalBtnText = "Next: Select Courses";
      }
    }
  },
  computed: {
    goBack() {
      this.$router.replace({ name: "learningjourney" });
    },
  },
  async mounted() {
    document.title = "LJMS - Update Learning Journey";
    // get LJ information from backend
    var LJInfo = await this.getLJInfo(this.currentLJ_ID);
    console.log(LJInfo)

    // load data into the v-model and array
    this.courses = LJInfo.data.data.Courses;
    // this.skills = LJInfo.datad.data.Skills;
    this.skills = ['egsg']

    // get role info
    var roleInfo = await this.getRoleInfo(LJInfo.data.data.Role_ID);
    this.role.role_name = roleInfo.data.data.Role_Name;
    this.role.role_description = roleInfo.data.data.Role_Description;

    // get skills info
    var skillInfo = await this.getSkillInfo(LJInfo.data.data.Role_ID);
    // this.skills = skillInfo.data.data;
    // this.skills.length == 0 ? (this.noSkillFound = true) : null;

    // get courses info
    var courseInfo = await this.getCourses();
    this.allCourses = courseInfo.data.data;
    this.allCourses.length == 0 ? (this.noCourseFound = true) : null;

    LJInfo
      ? (this.noLJFound = true)
      : (this.noLJFound = false);
  },
};
</script>

<style scoped>
  #updateLJMain {
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

  #roleDetails, #roleDetails > table{
    background-color: #404089;
    color: white;
  }

  .card-component {
    background-color: white;
    border-radius: 15px;
    cursor: pointer;
    transition: 0.2s;
    height: max-content;
    border: rgb(18, 18, 18) 2px solid;
    /* box-shadow: 0 3px 3px 0 rgb(0 0 0 / 4%), 0 5px 15px 0 rgb(0 0 0 / 4%); */
  }

  .card-component-header {
    display: flex;
    justify-content: space-between;
    background-color: transparent;
    align-items: center;
  }

  .card-title {
    display: -webkit-box;
    /* overflow: hidden; */
    word-wrap: break-word;
  }

  .card-body {
    /* max-height: 85px; */
    /* overflow: scroll; */
    display: block;
  }

  .card-text {
    display: -webkit-box;
    word-wrap: break-word;
  }

  #typeBadge {
    border: 2px solid #3e0b5e;
    color: #3e0b5e;
  }

  #catBadge {
    border: 2px solid #b43e8f;
    color: #b43e8f;
  }

  #addBtn, #backBtnModal {
    border: #434ce8 1px solid;
    color: #434ce8;
    transition: ease-in-out 0.5s;
  }

  #addBtn:hover, #backBtnModal:hover{
    background-color: #434ce8;
    color: #fbfbfb;
    transition: 0.2s ease-in-out;
  }

  #removeBtn, #nextBtnModal {
    background-color: #434ce8;
    border: none;
    color: #fbfbfb;
  }

  #removeBtn:hover, #nextBtnModal:hover  {
    background-color: #404089;
    transition: 0.2s ease-in-out;
  }

  #submitBtnModal {
    background-color: #b43e8f;
    border: none;
    color: #fbfbfb;
  }

  #submitBtnModal {
    background-color: #732173;
    transition: 0.2s ease-in-out;
  }
</style>
