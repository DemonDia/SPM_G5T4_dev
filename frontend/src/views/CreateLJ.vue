<template>
  <DashboardLayout>
    <div class="container-fluid p-sm-5" id="createLJMain">
      <div
        class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body"
      >
        <!-- Header -->
        <h3>Create a Learning Journey</h3>
        <h6 class="text-secondary mt-3 mb-3">
          Let's kickstart your learning journey!
        </h6>

        <!-- Popup -->
        <div v-show="checked">
          <ModalComponent
            type="role"
            :isSuccess="isSuccess"
            func="create"
            @clicked="onClickModal"
          />
        </div>

        <!-- Progress Tracker -->
        <div class="row gx-4 progress p-0">
          <div
            class="col-12 col-md-6"
            v-for="(value, key) in progress"
            :key="key"
          >
            <div class="row">
              <div
                class="progressbar mb-3"
                :style="[
                  this.currFormPg > key
                    ? { 'background-color': value.bg }
                    : { 'opacity': 0.1 },
                ]"
              ></div>
              <div class="row">
                <p
                  class="mb-0 fw-bold"
                  :style="[
                    this.currFormPg > key
                      ? { color: 'black' }
                      : { opacity: 0.4 },
                  ]"
                >
                  {{ value.title }}
                </p>
              </div>
              <div class="row">
                <p
                  :style="[
                    this.currFormPg > key
                      ? { color: 'black' }
                      : { opacity: 0.4 },
                  ]"
                >
                  {{ value.description }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Content -->
        <form @submit.prevent="handleSubmit" method="POST">
          <!-- Page 1 -->
          <div 
            id="formPg1"
            v-if="this.currFormPg == 1" 
            @reload="reload()"
            class="my-4 mx-auto"
          >
            <!-- Spinner -->
            <div v-if="this.roles.length < 1 && noRoleFound==false">
              <SpinnerComponent/>
            </div>
            <!-- Role Selection -->
            <div v-else>
              <div class="text-center fw-bold my-2">
                You have selected: 
                <span id="selected">{{this.selectedRname}}</span>
              </div>
              <div id="tiles" class="d-sm-block d-md-flex flex-wrap justify-content-around">
                <div 
                  v-for="(value, key) in this.roles" 
                  :key="key"
                  class="p-1 overflow-scroll d-sm-block d-md-inline-block"
                >
                  <TileComponent 
                    :id="value.Role_ID"
                    :name="value.Role_Name"
                    type="radio"
                    @clicked="onClickTile"
                  >
                  </TileComponent>
                </div>
              </div>
            </div>
            <!-- No Role Found -->
            <div v-show="noRoleFound" class="fs-3 fw-bold text-center align-middle pt-5 my-5">
              Sorry! No role found!
            </div>
          </div>

          <!-- Page 2 -->
          <div 
            id="formPg2"
            v-if="this.currFormPg == 2" 
            class="my-4 mx-auto"
          >
            <!-- Spinner -->
            <div v-if="this.courses.length < 1 && noCourseFound==false">
              <SpinnerComponent/>
            </div>
            <!-- Role Selection -->
            <div v-else>
              <div class="text-center fw-bold my-2">
                You have selected: 
                <span 
                  id="selected" 
                  v-for="(value,key) in this.selectedCname" 
                  :key="key"
                >
                  {{value}}
                </span>
              </div>
              <div id="tiles" class="d-sm-block d-md-flex flex-wrap justify-content-around">
                <div 
                  v-for="(value, key) in this.courses" 
                  :key="key"
                  class="p-1 overflow-scroll d-sm-block d-md-inline-block"
                >
                  <TileComponent 
                    :id="value.Course_ID"
                    :name="value.Course_Name"
                    type="checkbox"
                    @clicked="onClickTile"
                  >
                  </TileComponent>
                </div>
              </div>
            </div>
            <!-- No Course Found -->
            <div v-show="noCourseFound" class="fs-3 fw-bold text-center align-middle pt-5 my-5">
              Sorry! No course found!
            </div>
          </div>
        </form>

        <!-- Buttons -->
        <div class="row d-flex justify-content-around my-sm-3 my-md-5 p-3">
          <!-- First Button -->
          <button
            type="button"
            class="btn col-md-4 col-sm-6 m-2"
            :class="[
              this.currFormPg == 1
                ? 'btn-outline-secondary disabled'
                : 'btn-primary',
              this.isSubmitted && this.isSuccess ? 'disabled' : '',
            ]"
            @click="goToPrevPg"
          >
            {{ this.progress[currFormPg - 1].button1 }}
          </button>

          <!-- Second Button -->
          <button
            type="button"
            class="btn col-md-4 col-sm-5 m-2 order-sm-last order-first"
            :class="[
              this.currFormPg == 2 ? 'btn-warning' : 'btn-primary',
              this.isSubmitted && this.isSuccess ? 'disabled' : '',
            ]"
            @click="goToNextPg"
            :data-bs-toggle="this.currFormPg == 2 ? 'modal' : ''"
            :data-bs-target="this.currFormPg == 2 ? '#submitModal' : ''"
          >
            {{ this.progress[currFormPg - 1].button2 }}
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
  import SpinnerComponent from "@/components/SpinnerComponent.vue";
  import TileComponent from "@/components/TileComponent.vue";
  
  export default {
    name: "LJView",
    components: {
      DashboardLayout,
      FormComponent,
      ModalComponent,
      SpinnerComponent,
      TileComponent,
    },
    data() {
      return {
        roles: [],
        courses: [{Course_ID: 1, Course_Name: "dummy1"}, {Course_ID: 2, Course_Name: "dummy2"}],
        noRoleFound: false,
        noCourseFound: false,
        selectedR: "",
        selectedRname: "",
        selectedC: [],
        selectedCname: [],
        isSuccess: false,
        isSubmitted: false,
        checked: false,
        currFormPg: 1,
        progress: [
          {
            title: "STEP 1",
            bg: "#e4afff",
            description: "Select a role",
            button1: "Back to Step 1",
            button2: "Next: Select Courses",
          },
          {
            title: "STEP 2",
            bg: "#c86bfa",
            description: "Select courses",
            button1: "Back to Step 1",
            button2: "Submit",
          },
        ],
        pillItemsFromComponent: [],
      };
    },

    methods: {
      async reload() {
        this.pillItemsFromComponent = [];
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/available";
        await axios.get(url).then((response) => {
          var result = response.data.data;
          if (result.length == 0) {
            this.noRoleFound = true;
          }
          else {
            this.roles = result;
          }
        });
      },

      async loadCourses() {
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/course/available";
        await axios.get(url).then((response) => {
          var result = response.data.data;
          console.log(result)
          if (result.length == 0) {
            this.noCourseFound = true;
          }
          else {
            this.courses = result;
          }
        });
      },

      handleSubmit() {
        this.createLJ().then((res) => {
          var roleStatus = res.data;
          this.assignSkills(roleStatus.data).then((result) => {
            var assignSkillStatus = result.data;
            this.resetErrors();
            if (roleStatus.success || assignSkillStatus.success) {
              this.resetForm();
              this.isSuccess = true;
            } else {
              this.isSuccess = false;
              for (let err in roleStatus.message) {
                let msg = roleStatus.message[err];
                if (this.RNerrors.includes(msg)) {
                  this.role_name.errors.push(msg);
                } else {
                  this.role_description.errors.push(msg);
                }
              }
              // go back to form pg 1
              this.currFormPg = 1;
            }
            // show Modal
            this.checked = true;
          });
        });
      },
      
      createLJ() {
        var createLJUrl =
          "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/";
        return new Promise((resolve, reject) => {
          axios
            .post(createLJUrl, {
              // Role_Name: this.role_name.role_name,
              // Role_Description: this.role_description.role_description,
              // Active: true,
            })
            .then((response) => {
              resolve(response);
            })
            .catch((err) => reject(err));
        });
      },
      
      onClickModal(value) {
        this.checked = value;
        if (this.isSubmitted && this.isSuccess) {
          this.$router.replace({ name: "learningjourney" });
        }
      },

      onClickTile(value) {
        if (value.type == 'radio') {
          this.selectedR = value.id;
          this.selectedRname = value.name;
        } else if (value.type == 'checkbox') {
          this.selectedC.push(value.id);
          this.selectedCname.push(value.name)
        }
      },

      goToPrevPg() {
        this.currFormPg -= 1;
      },

      goToNextPg() {
        if (this.currFormPg == 2) {
          this.handleSubmit();
        } else {
          this.currFormPg += 1;
        }

      },

      goToPg(x) {
        this.currFormPg = x;
      },

      resetErrors() {
        // this.role_name.errors = [];
        // this.role_description.errors = [];
        // this.isSubmitted = NaN;
        // this.isSuccess = NaN;
        // this.checked = NaN;
        // this.pillItemsFromComponent = []
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
    },
    
    mounted() {
      document.title = "LJMS - Create Learning Journey";
      this.reload();
    },
  };
</script>
  
<style scoped>
  #createLJMain {
    min-height: 100vh;
  }

  .progress {
    height: fit-content;
    background-color: whitesmoke;
    font-size: 15px;
    margin: 5px 0;
  }

  .progressbar {
    border-radius: 2px;
    height: 8px;
  }

  #formPg1, #formPg2 {
    height: 38vh;
  }

  #tiles {
    height: 35vh;
    overflow-x: hidden;
    overflow-y: scroll;
  }

  .btn-primary {
    background-color: #434ce8;
    color: #fbfbfb;
    border: 0px;
  }

  .btn-primary:hover {
    background-color: #404089 !important; 
    transition: 0.2s ease-in-out;
  }

  .btn-warning {
    background-color: #fdd023;
    border: 0px;
  }

  .btn-warning:hover, .btn-warning:focus {
    background-color: #e9b200 !important;
    transition: 0.2s ease-in-out;
  }

  #selected {
    color: #404089;
  }
</style>