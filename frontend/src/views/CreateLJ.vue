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
            type="learning journey"
            :isSuccess="isSuccess"
            func="create"
            @clicked="onClickModal"
          />
        </div>

        <!-- Progress Tracker -->
        <div class="row gx-4 progress p-0">
          <div
            class="col-12 col-sm-4"
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
            class="my-4 mx-auto formPage"
          >
            <!-- Spinner -->
            <div v-if="this.roles.roles.length < 1 && noRoleFound==false">
              <SpinnerComponent/>
            </div>
            <!-- Role Selection -->
            <div v-else v-if="!noRoleFound">
              <div class="text-sm-start text-md-center fw-bold my-2">
                You have selected: 
                <span id="selected">{{this.selectedRname}}</span>
              </div>
              <div 
                id="tiles" 
                class="d-sm-inline-flex d-md-flex flex-wrap justify-content-around"
              >
                <div 
                  v-for="(value, key) in this.roles.roles" 
                  :key="key"
                  class="p-1 overflow-scroll"
                >
                  <TileComponent 
                    :id="value.Role_ID"
                    :name="value.Role_Name"
                    type="radio"
                    @clicked="onClickTile"
                    :selected="this.selectedR"
                  >
                  </TileComponent>
                </div>
              </div>
            </div>
            
            <!-- No Role Found -->
            <div v-show="noRoleFound" class="fs-3 fw-bold text-center align-middle pt-5 my-4">
              Sorry! No role found!
            </div>

            <!-- Role Error -->
            <div 
              v-show="this.roles.errorMsg != ''" 
              class="text-sm-start text-md-center text-danger fw-bold my-3 fs-5"
            >
              {{this.roles.errorMsg}}
            </div>
          </div>

          <!-- Page 2 -->
          <div 
            id="formPg2"
            v-if="this.currFormPg == 2"
            class="my-4 mx-auto formPage"
          >
            <!-- Spinner -->
            <div v-if="this.courses.courses.length < 1 && noCourseFound==false">
              <SpinnerComponent/>
            </div>
            <!-- Course Selection -->
            <div v-else v-if="!noCourseFound">
              <div class="text-sm-start text-md-center fw-bold my-2">
                You have selected: 
                <span 
                  id="selected" 
                >
                  {{this.selectedCname.join(', ')}}
                </span>
              </div>
              <div 
                id="tiles"
                class="d-sm-inline-flex d-md-flex flex-wrap justify-content-around"
              >
                <div 
                  v-for="(value, key) in this.courses.courses" 
                  :key="key"
                  class="p-1 overflow-scroll d-sm-block d-md-inline-block"
                >
                  <TileComponent 
                    :id="value.Course_ID"
                    :name="value.Course_Name"
                    type="checkbox"
                    @clicked="onClickTile"
                    :selected="this.selectedC"
                  >
                  </TileComponent>
                </div>
              </div>
            </div>
            
            <!-- No Course Found -->
            <div v-show="noCourseFound" class="fs-3 fw-bold text-center align-middle pt-5 my-4">
              Sorry! No course found!
            </div>

            <!-- Course Error -->
            <div 
              v-show="this.courses.errorMsg != ''" 
              class="text-sm-start text-md-center text-danger fw-bold my-3 fs-5"
            >
              {{this.courses.errorMsg}}
            </div>
          </div>

          <!-- Page 3 -->
          <div 
            id="formPg3"
            v-show="this.currFormPg == 3"  
            class="my-4 mx-auto formPage"
          >
            <p class="fw-bold mt-1 mb-0">Role Name</p>
            <p class="text-break">{{selectedRname}}</p>
            <p class="fw-bold mb-0">Selected Courses</p>
            <p class="text-break">{{selectedCname.join(', ')}}</p>
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
              this.disableBtn && this.isSuccess ? 'disabled' : '',
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
              this.currFormPg == 3 ? 'btn-warning' : 'btn-primary',
              this.disableBtn ? 'disabled' : '',
            ]"
            @click="goToNextPg"
            :data-bs-toggle="this.currFormPg == 3 ? 'modal' : ''"
            :data-bs-target="this.currFormPg == 3 ? '#submitModal' : ''"
          >
            {{ this.progress[currFormPg - 1].button2 }}
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
  import SpinnerComponent from "@/components/SpinnerComponent.vue";
  import TileComponent from "@/components/TileComponent.vue";
  import { mapGetters } from "vuex";
import { createToast } from 'mosha-vue-toastify';
  
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
        roles: {
          roles: [],
          errorMsg: "",
        },
        courses: {
          courses: [],
          errorMsg: "",
        },
        // LJRoleErrors: [],
        noRoleFound: false,
        noCourseFound: false,
        selectedR: "",
        lastSavedR: NaN,
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
            button2: "Next: Confirm choices",
          },
          {
            title: "STEP 3",
            bg: "#2d0f51",
            description: "Summary",
            button1: "Back to Step 2",
            button2: "Submit",
          },
        ],
        disableBtn: false,
      };
    },

    methods: {
      async reload() {
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/available";
        await axios.get(url).then((response) => {
          var result = response.data.data;
          if (result.length == 0) {
            this.noRoleFound = true;
          }
          else {
            this.noRoleFound = false;
            this.roles.roles = result;
          }
        });
      },

      loadCourses() {
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/courses/" + this.selectedR;
        axios.get(url).then((response) => {
          var result = response.data.data;
          if (result.length == 0) {
            this.noCourseFound = true;
          }
          else {
            this.noCourseFound = false;
            this.courses.courses = result;
          }
        });
      },

      handleSubmit() {
        console.log('form submitted')
        this.isSubmitted = true;
        this.createLJ().then((res) => {
          var LJStatus = res.data;
          if (LJStatus.success) {
            this.resetForm();
            this.isSuccess = true;
          } else {
            this.isSuccess = false;
            this.currFormPg = 1;
          }
          // show Modal
          this.checked = true;
        });
      },
      
      createLJ() {
        var createLJUrl =
          "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/learningjourney/";
        return new Promise((resolve, reject) => {
          axios
            .post(createLJUrl, {
              Staff_ID: this.user.StaffID,
              Courses: this.selectedC,
              Role_ID: this.selectedR,
            })
            .then((response) => {
              resolve(response);
            })
            .catch((err) => reject(err));
        });
      },
      
      onClickModal(value) {
        this.checked = value;
        if (this.isSuccess) {
          this.disableBtn = true;
          this.$router.replace({ name: "learningjourney" });
        }
      },

      onClickTile(value) {
        // store / update selection
        if (value.type == 'radio') {
          this.selectedR = value.id;
          this.selectedRname = value.name;
          this.loadCourses();
        } else if (value.type == 'checkbox') {
          if (this.selectedC.includes(value.id)) {
            let indexC = this.selectedC.indexOf(value.id);
            let indexCname = this.selectedCname.indexOf(value.name);
            this.selectedC.splice(indexC, 1);
            this.selectedCname.splice(indexCname, 1);
          } else {
            this.selectedC.push(value.id);
            this.selectedCname.push(value.name);
          }
        }
        // update disabled button property
        if (this.disableBtn) {
          this.checkForm();
        }
      },

      goToPrevPg() {
        this.currFormPg -= 1;
        // if go back to change role (pg 1), reset noCourseFound to false
        if (this.currFormPg == 1) {
          if (this.lastSavedR != this.selectedR) {
            this.courses.courses = [];
            this.loadCourses();
          }
        }
        this.checkForm();
      },

      goToNextPg() {
        // form validation
        let status = this.checkForm();
        if (status) {
          if (this.currFormPg < 3) {
            this.currFormPg += 1;
            if (this.lastSavedR == NaN) {
              // save role
              this.lastSavedR = this.selectedR;
            }
          } else {
            this.handleSubmit();
          }
        }
      },

      checkForm() {
        let cond1 = this.selectedR == "";
        let cond2 = (this.selectedC).length < 1;
        // validation
        if ((this.currFormPg == 1 && cond1)  ||  (this.currFormPg == 2 && cond2)  || (this.currFormPg == 3 && (cond1 || cond2)) ){
          this.createErrorMsg(cond1, cond2);
          this.disableBtn = true;
          return false;
        }
        // no problemo
        this.resetErrors();
        this.disableBtn = false;
        return true;
      },

      resetErrors() {
        this.roles.errorMsg = "";
        this.courses.errorMsg = "";
      },

      resetForm() {
        this.isSubmitted = NaN;
        this.isSuccess = NaN;
        this.checked = NaN;
      },

      createErrorMsg(cond1, cond2) {
        if (cond1) {
          this.roles.errorMsg = "Please select a role to begin";
        } else if (cond2 && this.noCourseFound) {
          this.courses.errorMsg = "Please go back and choose a role with at least one course available"
        } else if (cond2) {
          this.courses.errorMsg = "You need at least one course to create a learning journey";
        }
        
        else {
          // no error
          this.roles.errorMsg = "";
          this.courses.errorMsg = "";
        }
      },

      getRoleInfo(role_id) {
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/" + role_id;
        return new Promise((resolve, reject) => {
          axios.get(url).then((response) => { resolve(response.data.data); }).catch((err) => reject(err)); });
      },
    },
    
    computed: {
      ...mapGetters({
        user: "auth/user",
        authenticated: "auth/authenticated",
      }),
    },
    
    async mounted() {
      document.title = "LJMS - Create Learning Journey";
      this.reload();
      if (this.$route.params.role_id) {
        var roleInfo = await this.getRoleInfo(this.$route.params.role_id);
        if (roleInfo) {
          this.selectedR = roleInfo.Role_ID;
          this.lastSavedR = roleInfo.Role_ID;
          this.selectedRname = roleInfo.Role_Name;
          this.loadCourses();
          this.currFormPg = 2;
        }
      }
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

  .formPage {
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