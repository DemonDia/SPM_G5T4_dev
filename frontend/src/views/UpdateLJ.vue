<template>
  <DashboardLayout>
    <div class="container-fluid p-sm-5" id="updateLJMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="isNaN(this.noLJFound)" />

      <!-- No LJ Found -->
      <div v-else-if="!(this.noLJFound)" class="fs-3 fw-bold text-center align-middle pt-5 my-5">
        Sorry, can't find this Learning Journey. Please try again!
      </div>

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

        <!-- Success/Error Popup -->
        <div v-show="checked">
          <ModalComponent
            type="learning journey"
            func="update"
            :isSuccess="isSuccess"
            @clicked="onClickModal"
          />
        </div>

        <!-- Add Course to LJ Popup -->
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
              <div v-if="!this.noNewCoursesAvail">
                <div class="modal-body my-1 text-center">
                  <!-- Error -->
                  <div 
                    v-show="this.errorMsg.length > 0" 
                    class="text-danger fw-bold my-3 fs-5"
                  >
                    {{this.errorMsg}}
                  </div>
                  <!-- Rest of Content -->
                  {{addCourseModalContent[1].modalDesc}}
                  <div 
                    v-for="(value, key) in this.coursesForSkills"
                    :key="key"
                    class="p-1 py-3 overflow-hidden d-sm-block d-md-inline-block"
                  >
                    <TileComponent 
                      :id="value.Course_ID"
                      :name="value.Course_Name"
                      type="checkbox"
                      itemType="course"
                      @clicked="onClickTile"
                      :selected="this.selectedC"
                    >
                    </TileComponent>
                  </div>
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
              <div v-else>
                <div class="modal-body fs-4 fw-bold text-center align-middle p-5 my-3">
                  Sorry, there are no more courses left to add!
                </div>
                <div class="modal-footer">
                  <button 
                    class="btn" 
                    data-bs-toggle="modal" 
                    data-bs-dismiss="modal"
                    id="nextBtnModal"
                  >
                    Close
                  </button>
                </div>
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
              <div class="modal-body my-1">
                {{addCourseModalContent[2].modalDesc}}
                <div v-if="this.selectedCname.length > 1" class="py-1">
                  <ol>
                    <li 
                      v-for="(value,key) in this.selectedCname" 
                      :key="key" 
                      class="fw-bold my-1"
                    >
                      {{value}}
                    </li>
                  </ol>
                </div>
                <div v-else class="py-1">
                  <p class="fw-bold my-1">{{this.selectedCname[0]}}</p>
                </div>
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
                  data-bs-target="#submitModal" 
                  data-bs-toggle="modal" 
                  data-bs-dismiss="modal"
                  @click="handleSubmitAdd()"
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
                  <p class="m-0 pb-0 fw-bolder">Selected Role</p>
                </th>
                <td class="col">
                  <p class="m-1 my-0 p-1 fw-bold">{{this.role.role_name}}</p>
                  <p class="m-1 my-0 p-1 fst-italic">{{this.role.role_description}}</p>
                </td>
              </tr>
              <tr class="row">
                <th class="col-sm-6 col-md-3">
                  <p class="m-0 pb-0 fw-bolder">Selected Skills</p>
                </th>
                <td class="col" v-for="(value,key) in this.skills" :key="key">
                  <p class="m-1 my-0 p-1 fw-bold"> {{ value.Skill_Name }} </p>
                  <p class="m-1 my-0 p-1 fst-italic"> {{ getSkillInfo(value, "desc") }} </p>
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
              @click="addModalClicked()" 
              data-bs-toggle="modal" 
              data-bs-target="#addCourseModal"
              @mouseover="hoverText='+ Add a new course'" 
              @mouseleave="hoverText='+'"
            >
              {{hoverText}}
            </button>
            <!-- See existing courses -->
            <div v-for="(value, key) in this.courses" v-bind:key="key" class="card-component row mx-1 my-3">
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
                <button type="button" class="btn mx-auto" id="removeBtn" @click="handleSubmitRemove(value.Course_ID)">
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
import TileComponent from "@/components/TileComponent.vue";
import ModalComponent from "@/components/ModalComponent.vue";
import { createToast } from 'mosha-vue-toastify';

export default {
  name: "UpdateLJ",
  components: {
    DashboardLayout,
    FormComponent,
    SpinnerComponent,
    TileComponent,
    ModalComponent,
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
      skillIDs: [],
      allSkills: [], // all available in database
      allCourses: [], // all available in database
      coursesForSkills: [], // to show in modal to add
      selectedC: [], // newly added selection
      selectedCname: [], // newly added selection
      errorMsg: "",
      checked: NaN,
      isSuccess: NaN,
      isSubmitted: NaN,
      noLJFound: NaN,
      noCourseFound: false,
      noSkillFound: false,
      currentLJ_ID: this.$route.params.lj_id,
      addCourseActive: false,
      addCourseModalContent: {
        1: {
          modalTitle: "Select new courses",
          modalDesc: "Select courses you wish to add to this learning journey"
        },
        2: {
          modalTitle: "Confirm selection",
          modalDesc: "You have added these courses to your learning journey:"
        }
      },
      hoverText: '+',
      modalBtnText: "Next: Confirm selection",
      noNewCoursesAvail: false, // to see if there are available courses to add
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

    getAvailSkills() {
      var getSkillUrl = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/available";
      return new Promise((resolve, reject) => {
        axios
          .get(getSkillUrl)
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

    getSkillInfo(skill, resultType) {
      let id = skill.Skill_ID;
      // store skill id into arr
      if (!this.skillIDs.includes(id)) {
        this.skillIDs.push(id);
      }
      // find skill details
      let filtered = this.allSkills.filter(function(skill) {return skill.Skill_ID==id})[0];
    
        if (resultType == "desc") {
          return filtered.Skill_Description
        }

    },

    getAvailCourses() {
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
        } else if (resultType == "desc") {
          return course.Course_Desc
        } 
  
    },

    onClickModal() {
      // modal is closed
      if (this.isSuccess) {
        // refresh page
        // this.resetErrors();
        // go back to View All
        this.$router.replace({ name: "learningjourney" });
      }
    },

    resetErrors() {
      // reset fields
      this.isSubmitted = NaN;
      this.isSuccess = NaN;
      this.checked = NaN;
      this.noLJFound = NaN;
      // reload stuff
      this.loadCourses();
      var LJInfo = this.getLJInfo(this.currentLJ_ID);
      this.noLJFound = LJInfo.data.success;
      // load data into the v-model and array
      this.courses = LJInfo.data.data.Courses;
      // skip getting role, skills and courses info
    },

    addModalClicked() {
      this.addCourseActive = false;
      this.filterCourses();
    },

    onClickTile(value) {
      // store / update selection
      let obj = {'Course_ID': value.id, 'Course_Name': value.name};
      let indexC = this.selectedC.findIndex((course) => course.Course_ID==value.id);
      let indexCname = this.selectedCname.findIndex((course) => course.Course_ID==value.name);
      if (indexC > -1) {
        this.selectedC.splice(indexC, 1);
        this.selectedCname.splice(indexCname, 1);
      } else {
        this.selectedC.push(obj);
        this.selectedCname.push(value.name);
      }
    },

    loadCourses() {
      var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skillcourserelations/byid";
      axios.post(url, {"Skills": this.skillIDs}).then((response) => {
        var result = response.data.data;
        if (result.length == 0) {
          this.noCourseFound = true;
        }
        else {
          this.noCourseFound = false;
          this.coursesForSkills = result;
        }
      }).catch((error) => {
        this.noCourseFound = true;
      });
    },

    filterCourses() {
      // get courses that are not already in the LJ
      var filterByReference = (arr1, arr2) => {
        let res = [];
        res = arr1.filter(el => {
            return !arr2.find(element => {
              return element.Course_ID === el.Course_ID;
            });
        });
        return res;
      }
      this.coursesForSkills = filterByReference(this.coursesForSkills, this.courses);
      if (this.coursesForSkills.length == 0) {
        this.noNewCoursesAvail = true;
      }
      this.addCourseActive = true;
    },

    handleSubmitAdd() {
      this.isSubmitted = true;
      if (this.selectedC.length > 0) {
        this.errorMsg = "";
        this.addCoursetoLJ().then((res) => {
          var LJStatus = res.data;
          if (LJStatus.success) {
            this.isSuccess = true;
            this.addCourseActive = false;
            // show Modal
            this.checked = true;
          }
        });
      } else {
        this.errorMsg = "Please ensure that at least one course is selected.";
      }
    },

    addCoursetoLJ() {
      var addCourseLJUrl =
        "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/courselearningjourney/";
      let selectedCId = this.selectedC.map(value => value.Course_ID);
      return new Promise((resolve, reject) => {
        axios
          .post(addCourseLJUrl, {
            LearningJourney_ID: this.currentLJ_ID,
            Courses: selectedCId,
          })
          .then((response) => {
            resolve(response);
          })
          .catch((err) => reject(err));
      });
    },

     handleSubmitRemove(id) {
      var currCourseLen = this.courses.length;
      if (currCourseLen > 1) {
        var removeStatus =  this.removeCoursefromLJ(id);
        if (removeStatus) {
          createToast('Course removed successfully!', {
            type: 'success',
            position: 'top-center',
            timeout: 3000,
            dismissible: true,
            pauseOnFocusLoss: true,
            pauseOnHover: true,
            closeOnClick: true,
            closeButton: true,
            icon: true,
            rtl: false,
            toastBackgroundColor: '#57cc99',
          });
          this.resetErrors();
        } else {
          createToast('Course cannot be removed!', {
            type: 'danger',
            position: 'top-center',
            timeout: 3000,
            dismissible: true,
            pauseOnFocusLoss: true,
            pauseOnHover: true,
            closeOnClick: true,
            closeButton: true,
            icon: true,
            rtl: false,
            toastBackgroundColor: '#d5465c',
          });
        }
      } else {
        // reject removal - need to keep at least one
        createToast('Learning Journeys must have at least one course!', {
          type: 'warning',
          position: 'top-center',
          timeout: 3000,
          dismissible: true,
          pauseOnFocusLoss: true,
          pauseOnHover: true,
          closeOnClick: true,
          closeButton: true,
          icon: true,
          rtl: false,
          toastBackgroundColor: '#d5465c',
        });
      }
    },

    removeCoursefromLJ(id) {
        var dltCourseLJUrl = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/courselearningjourney/delete";
        axios.post(dltCourseLJUrl, {
          'LearningJourney_ID': this.currentLJ_ID,
          'Course_ID': id,
        }).then((response) => {
          var result = response.data.success
          if (result) {
            return true
          }
         return false
        }).catch (error => {
          return false
        });

    },
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
    this.noLJFound = LJInfo.data.success;

    // load data into the v-model and array
    this.courses = LJInfo.data.data.Courses;
    this.skills = LJInfo.data.data.Skills;

    // get role info
    var roleInfo = await this.getRoleInfo(LJInfo.data.data.Role_ID);
    this.role.role_name = roleInfo.data.data.Role_Name;
    this.role.role_description = roleInfo.data.data.Role_Description;

    // get skills info
    var availSkills = await this.getAvailSkills();
    this.allSkills = availSkills.data.data;
    this.allSkills.length == 0 ? (this.noSkillFound = true) : null;

    // get courses info
    var availCourses = await this.getAvailCourses();
    this.allCourses = availCourses.data.data;

    this.loadCourses();
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

  #submitBtnModal:hover {
    background-color: #732173;
    transition: 0.2s ease-in-out;
  }

  .modal {
    transition: all .75s ease;
  }
</style>
