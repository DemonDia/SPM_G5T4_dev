<template>
    <DashboardLayout>
      <div class="container-fluid p-sm-5" id="createSkillMain">
        <div
        class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body"
        >
          <!-- Header -->
          <h3>Create a Skill</h3>
          <h6 class="text-secondary mt-3 mb-3">
            What skill would you like to create today?
          </h6>

          <!-- Modal -->
          <div v-show="checked">
            <ModalComponent 
            type="Skill" 
            :isSuccess="isSuccess" 
            func="create"
            @clicked="onClickModal"
          />
          </div>

          <!-- Progress Tracker -->
          <div class="row gx-4 progress p-0">
            <div
              class="col-12 col-md-4"
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
    
          <!-- Form -->
          <form @submit.prevent="handleSubmit" method="POST">

            <!-- Page 1 -->
            <div v-show="this.currFormPg == 1" id="formPg1">
              <FormComponent
                v-model="skill_name.skill_name"
                :label="skill_name.label"
                type="text"
                :limit="skill_name.limit"
                :errors="skill_name.errors"
                :isSubmitted="isSubmitted"
                :formType="skill_name.formType"
              /> 
              <FormComponent
                v-model="skill_description.skill_description"
                :label="skill_description.label"
                type="text"
                :limit="skill_description.limit"
                :errors="skill_description.errors"
                :isSubmitted="isSubmitted"
                :formType="skill_description.formType"
              />
            </div>

            <!-- Page 2 -->
            <div v-show="this.currFormPg == 2" id="formPg2">
              <PillSearchComponent
                class="my-5"
                ctype="role"
                @pillItems="getPill"
              ></PillSearchComponent>
            </div>

            <!-- Page 3 -->
            <div v-show="this.currFormPg == 3" id="formPg3"  class="mt-2 pt-1 mb-0">
              <p class="fw-bold">Skill Name</p>
              <p class="text-break">{{ skill_name.skill_name }}</p>
              <p class="fw-bold">Skill Description</p>
              <p class="text-break">{{ skill_description.skill_description }}</p>
              <p class="fw-bold mb-0">Roles</p>
              <pill-component :pillList="pillValue" />
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
              class="btn col-md-4 col-sm-5 m-2"
              :class="[
                this.currFormPg == 3 ? 'btn-warning' : 'btn-primary',
                this.isSubmitted && this.isSuccess ? 'disabled' : '',
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
    import PillSearchComponent from "@/components/PillSearchComponent.vue";
    import PillComponent from "@/components/PillComponent.vue";
  
    export default {
      name: "CreateSkill",
      components: {
        DashboardLayout,
        FormComponent,
        ModalComponent,
        PillSearchComponent,
        PillComponent,
      },
      data() {
        return {
          skill_name: {
            skill_name: "",
            label: "Skill Name",
            limit: "30",
            errors: [],
            formType: "input",
          },
          skill_description: {
            skill_description: "",
            label: "Skill Description",
            limit: "170",
            errors: [],
            formType: "textarea",
          },
          isSuccess: false,
          isSubmitted: false,
          checked: false,
          SNerrors: [
            "Skill Name cannot be empty! Please try again",
            "Skill already exists! Please try again",
            "Skill Name exceeds character limit of 30! Please try again"
          ],
          currFormPg: 1,
          progress: [
            {
              title: "STEP 1",
              bg: "#e4afff",
              description: "Input skill details",
              button1: "Back to Step 1",
              button2: "Next: Assign Roles",
            },
            {
              title: "STEP 2",
              bg: "#c86bfa",
              description: "Assign skills (optional)",
              button1: "Back to Step 1",
              button2: "Next: Confirm summary",
            },
            {
              title: "STEP 3",
              bg: "#2d0f51",
              description: "Confirm summary",
              button1: "Back to Step 2",
              button2: "Submit",
            },
          ],
          pillItemsFromComponent: [],
        };
      },
      methods: {
        handleSubmit() {
          this.createSkill().then((res) => {
            var roleStatus = res.data;
            this.assignSkills(roleStatus.data).then((result) => {
              var assignSkillStatus = result.data;
              
              this.resetErrors();
              if (roleStatus.success || assignSkillStatus.success) {
                this.resetForm(); // throw error message if role is duplicated
                this.isSuccess = true;
              } else {
                // failure case
                this.isSuccess = false;
                for (let err in roleStatus.message) {
                  let msg = roleStatus.message[err];
                  if (this.SNerrors.includes(msg)) {
                    this.skill_name.errors.push(msg);
                  } else {
                    this.skill_description.errors.push(msg);
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

        createSkill() {
          var createRoleUrl = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/"
          return new Promise((resolve, reject) => {
          axios
            .post(createRoleUrl, {
              Skill_Name: this.skill_name.skill_name,
              Skill_Description: this.skill_description.skill_description,
              Active: true,
            })
            .then((response) => {
              resolve(response);
            })
            .catch((err) => reject(err));
          });
        },

        assignSkills(skill_id) {
          var assignRolesUrl =
            "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roleskillrelations/";
          return new Promise((resolve, reject) => {
            axios
              .post(assignRolesUrl, {
                Skill_ID: skill_id,
                Roles: this.pillRole_IDArray,
              })
              .then((response) => {
                resolve(response);
              })
              .catch((err) => reject(err));
          });
        },

        resetForm() {
          this.skill_name.skill_name = "";
          this.skill_description.skill_description = "";
        },

        onClickModal(value) {
          // modal is closed
          // reset checked value:
          this.checked = value;
          if (this.isSuccess) {
            // go back to View All
            this.$router.replace({ name: "skills" });
          }
        },

        goToPrevPg() {
          this.currFormPg -= 1;
        },

        goToNextPg() {
          if (this.currFormPg == 3) {
            // submit form
            this.handleSubmit();
          } else {
            this.currFormPg += 1;
          }
        },

        goToPg(x) {
          this.currFormPg = x;
        },

        getPill(item) {
          // emit content to be passed into the pillItemsFromComponent
          this.pillItemsFromComponent = item;
        },

        resetErrors() {
          // reset fields
          this.skill_name.errors = [];
          this.skill_description.errors = [];
          this.isSubmitted = NaN;
          this.isSuccess = NaN;
          this.checked = NaN;
          this.pillItemsFromComponent = []
        },
      },

      computed: {
        // This computed function will enumerate the pillItemsFromComponent where the key/value items is stored
        // And then it will return the value of the key "skill_name" to be displayed in the pill
        pillValue() {
          const pillItems = [];
          this.pillItemsFromComponent.forEach((value) => {
            pillItems.push(value.Role_Name);
          });
          return pillItems;
        },

        // This computed function will enumerate the pillItemsFromComponent where the key/value items is stored
        // And then it will return the value of the key "skill_id" and return to the assign skill function.
        pillRole_IDArray() {
          const pillItems = [];
          this.pillItemsFromComponent.forEach((value) => {
            pillItems.push(value.Role_ID);
          });
          return pillItems;
        },
      },

      mounted() {
        document.title = "LJMS - Create Skill";
      },
    };
  </script>
  
  <style scoped>
    #createSkillMain {
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
  
    #formPg1, #formPg2, #formPg3 {
      height: 30vh;
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
  </style>
  