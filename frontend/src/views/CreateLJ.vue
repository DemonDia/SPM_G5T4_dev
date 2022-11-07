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
            class="col-12 col-sm-3"
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
              <div class="text-sm-start text-md-center fw-bold my-2 px-3">
                You have selected: 
                <span id="selected">{{this.selectedRname}}</span>
              </div>
              <div 
                id="tiles" 
                class="d-sm-inline-flex d-md-flex flex-wrap justify-content-sm-start justify-content-md-center"
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
                    itemType="role"
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
            <div v-if="this.skills.skills.length < 1 && noSkillFound==false">
              <SpinnerComponent/>
            </div>
            <!-- Course Selection -->
            <div v-else v-if="!noSkillFound">
              <div class="text-sm-start text-md-center fw-bold my-2">
                You have selected: 
                <span 
                  id="selected" 
                >
                  {{this.selectedSname.join(', ')}}
                </span>
              </div>
              <div 
                id="tiles"
                class="d-sm-inline-flex d-md-flex flex-wrap justify-content-around"
              >
                <div 
                  v-for="(value, key) in this.skills.skills" 
                  :key="key"
                  class="p-1 overflow-scroll d-sm-block d-md-inline-block"
                >
                  <TileComponent 
                    :id="value.Skill_ID"
                    :name="value.Skill_Name"
                    type="checkbox"
                    itemType="skill"
                    @clicked="onClickTile"
                    :selected="this.selectedS"
                  >
                  </TileComponent>
                </div>
              </div>
            </div>
            
            <!-- No skill Found -->
            <div v-show="noSkillFound" class="fs-3 fw-bold text-center align-middle pt-5 my-4">
              Sorry! No skill found!
            </div>

            <!-- Skill Error -->
            <div 
              v-show="this.skills.errorMsg != ''" 
              class="text-sm-start text-md-center text-danger fw-bold my-3 fs-5"
            >
              {{this.skills.errorMsg}}
            </div>
          </div>

          <!-- Page 3 -->
          <div 
            id="formPg2"
            v-if="this.currFormPg == 3"
            class="my-4 mx-auto formPage"
          >
            <!-- Spinner -->
            <div v-if="this.courses.courses.length < 1 && noCourseFound==false">
              <SpinnerComponent/>
            </div>
            <!-- Course Selection -->
            <div v-else v-if="!noCourseFound">
              <div class="text-sm-start text-md-center fw-bold my-2 px-3">
                You have selected: 
                <span 
                  id="selected" 
                >
                  {{this.selectedCname.join(', ')}}
                </span>
              </div>
              <div 
                id="tiles"
                class="d-sm-inline-flex d-md-flex flex-wrap justify-content-sm-start justify-content-md-center"
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
                    itemType="course"
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

          <!-- Page 4 -->
          <div 
            id="formPg3"
            v-show="this.currFormPg == 4"  
            class="my-4 mx-auto formPage"
          >
            <p class="fw-bold mt-1 mb-0">Role Name</p>
            <p class="text-break">{{selectedRname}}</p>
            <p class="fw-bold mb-0">Selected Skills</p>
            <p class="text-break">{{selectedSname.join(', ')}}</p>
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
              this.currFormPg == 4 ? 'btn-warning' : 'btn-primary',
              this.disableBtn ? 'disabled' : '',
            ]"
            @click="goToNextPg"
            :data-bs-toggle="this.currFormPg == 4 ? 'modal' : ''"
            :data-bs-target="this.currFormPg == 4 ? '#submitModal' : ''"
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
        skills: {
          skills: [],
          errorMsg: "",
        },
        courses: {
          courses: [],
          errorMsg: "",
        },
        // LJRoleErrors: [],
        noRoleFound: false,
        noCourseFound: false,
        noSkillFound: false,
        selectedR: "",
        lastSavedR: NaN,
        selectedRname: "",
        selectedS: [],
        lastSavedS: [],
        selectedSname: [],
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
            button2: "Next: Select skills",
          },
          {
            title: "STEP 2",
            bg: "#c86bfa",
            description: "Select skills",
            button1: "Back to Step 1",
            button2: "Next: Select courses",
          },
          {
            title: "STEP 3",
            bg: "#a055c8",
            description: "Select courses",
            button1: "Back to Step 2",
            button2: "Next: Confirm choices",
          },
          {
            title: "STEP 4",
            bg: "#2d0f51",
            description: "Summary",
            button1: "Back to Step 3",
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

      loadSkills() {
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roleskillrelations/" + this.selectedR;
        axios.get(url).then((response) => {
          var result = response.data.data;
          if (result.length == 0) {
            this.noSkillFound = true;
          }
          else {
            this.noSkillFound = false;
            this.skills.skills = result;
          }
        }).catch((error) => {
          this.noSkillFound = true;
        });
      },

      loadCourses() {
        console.log("loading courses...")
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skillcourserelations/byid";
        axios.get(url, this.selectedS).then((response) => {
          console.log(response)
          var result = response.data.data;
          if (result.length == 0) {
            this.noCourseFound = true;
          }
          else {
            this.noCourseFound = false;
            this.courses.courses = result;
          }
        }).catch((error) => {
          console.log(error)
          this.noCourseFound = true;
        });
      },

      handleSubmit() {
        this.isSubmitted = true;
        this.createLJ().then((res) => {
          var LJStatus = res.data;
          console.log(LJStatus);
          console.log(this.user.StaffID)
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
          this.loadSkills();
        } else if (value.type == 'checkbox') {
          if(value.itemType == "course") {
            // selecting course
            if (this.selectedC.includes(value.id)) {
              let indexC = this.selectedC.indexOf(value.id);
              let indexCname = this.selectedCname.indexOf(value.name);
              this.selectedC.splice(indexC, 1);
              this.selectedCname.splice(indexCname, 1);
            } else {
              this.selectedC.push(value.id);
              this.selectedCname.push(value.name);
            }
          } else if (value.itemType == "skill") {
            // selecting skill
            if (this.selectedS.includes(value.id)) {
              let indexS = this.selectedS.indexOf(value.id);
              let indexSname = this.selectedSname.indexOf(value.name);
              this.selectedS.splice(indexS, 1);
              this.selectedSname.splice(indexSname, 1);
            } else {
              this.selectedS.push(value.id);
              this.selectedSname.push(value.name);
              this.loadCourses()
            }
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
        if (this.currFormPg == 1 && this.lastSavedR !== this.selectedR) {
          // reset skills
          this.skills.skills = [];
          // reset courses
          this.courses.courses = [];
          // reload skills
          this.loadSkills();
        } else if (this.currFormPg == 2 && this.lastSavedS !== this.selectedS) {
          // reset courses
          this.courses.courses = [];
          // reload courses
          this.loadCourses();
        }
        this.checkForm();
      },

      goToNextPg() {
        // form validation
        let status = this.checkForm();
        if (status) {
          if (this.currFormPg < 4) {
            this.currFormPg += 1;
            if (this.lastSavedR === NaN || isNaN(this.lastSavedR)) {
              // save role
              this.lastSavedR = this.selectedR;
            } else if (this.lastSavedS === NaN || isNaN(this.lastSavedS)) {
              // save skills
              this.lastSavedS = this.selectedS;
            }
          } else {
            this.handleSubmit();
          }
        }
      },

      checkForm() {
        let cond1 = this.selectedR == "";
        let cond2 = (this.selectedS).length < 1;
        let cond3 = (this.selectedC).length < 1;
        // validation
        if ((this.currFormPg == 1 && cond1) ||  (this.currFormPg == 2 && cond2) ||  (this.currFormPg == 3 && cond3)  || (this.currFormPg == 4 && (cond1 || cond2 || cond3)) ){
          this.createErrorMsg(cond1, cond2, cond3);
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
        this.skills.errorMsg = "";
      },

      resetForm() {
        this.isSubmitted = NaN;
        this.isSuccess = NaN;
        this.checked = NaN;
      },

      createErrorMsg(cond1, cond2, cond3) {
        if (cond1) {
          this.roles.errorMsg = "Please select a role to begin";
        } else if (cond2 && this.noSkillFound) {
          this.skills.errorMsg = "Please go back and choose a role with at least one skill available"
        } else if (cond2) {
          this.skills.errorMsg = "You need at least one skill to create a learning journey";
        } else if (cond3 && this.noCourseFound) {
          this.courses.errorMsg = "Please go back and choose a skill with at least one course available"
        } else if (cond3) {
          this.courses.errorMsg = "You need at least one course to create a learning journey";
        }
        
        else {
          // no error
          this.roles.errorMsg = "";
          this.courses.errorMsg = "";
          this.skills.errorMsg = "";
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
          this.loadSkills();
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