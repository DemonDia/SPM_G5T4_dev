<template>
    <DashboardLayout>
      <div class="container-fluid p-sm-5" id="updateSkillMain">
        <!-- Spinner -->
        <SpinnerComponent v-if="!noSkillFound" />
        
        <!-- Content -->
        <div
          v-else
          class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body"
        >
          <button @click="goBack" class="ph-arrow-left back-btn mb-3">
            Back
          </button>
          <h3>Update a Skill</h3>
          <h6 class="text-secondary mt-3 mb-3">
            Change the skill details or add/remove roles to this skill
          </h6>
  
          <!-- Popup -->
          <div v-show="checked">
            <ModalComponent
              type="skill"
              func="update"
              :isSuccess="isSuccess"
              @clicked="onClickModal"
            />
          </div>
  
          <!-- Content -->
          <form @submit.prevent="handleSubmit" method="POST">
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
  
            <PillSearchComponent
              class="mt-3"
              ctype="role"
              :skills="roles_array"
              @pillItems="getPill"
              func="search"
            ></PillSearchComponent>
          </form>
  
          <!-- Button -->
          <div class="row d-flex justify-content-around my-sm-3 my-md-5 p-3">
            <button
              type="button"
              class="btn col-md-4 col-sm-5 m-2 btn-primary"
              @click="handleSubmit"
              data-bs-toggle="modal"
              data-bs-target="#submitModal"
              id="submitBtn"
            >
              Update Skill
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
      name: "UpdateSkill",
      components: {
      DashboardLayout,
      FormComponent,
      ModalComponent,
      PillSearchComponent,
      PillComponent,
      SpinnerComponent
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
          RNerrors: [
            "Skill Name cannot be empty! Please try again",
            "Skill already exists! Please try again",
            "Skill Name exceeds character limit of 30! Please try again",
          ],
          pillItemsFromComponent: [],
          noSkillFound: false,
          roles_array: [],
          currentSkill_ID: this.$route.params.skill_id,
        };
      },
      methods: {
    
        handleSubmit() {
          // submitted form
          this.isSubmitted = true;
          this.updateskill(this.currentSkill_ID).then((res) => {
            var skillStatus = res.data;
            // check success
            console.log(skillStatus)
            if (skillStatus.success) {
              this.assignSkills(this.currentSkill_ID).then((result) => {
                this.resetErrors();
                // this.resetForm();
                this.isSuccess = true;
                this.checked = true; // show Modal
              });
            } else {
              this.isSuccess = false;
              for (let err in skillStatus.message) {
                let msg = skillStatus.message[err];
                if (this.RNerrors.includes(msg)) {
                  this.skill_name.errors.push(msg);
                } else {
                  this.skill_description.errors.push(msg);
                }
              }
              this.checked = true; // show Modal
            }
          });
        },
  
        updateskill(skill_id) {
          var updateskillUrl =
            "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/" +
            skill_id;
          return new Promise((resolve, reject) => {
            axios
              .put(updateskillUrl, {
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
          var assignSkillsUrl =
            "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skillrolerelations/" +
            skill_id;
          return new Promise((resolve, reject) => {
            axios
              .put(assignSkillsUrl, {
                Roles: this.pillRole_IDArray,
              })
              .then((response) => {
                resolve(response);
              })
              .catch((err) => reject(err));
          });
        },
  
        getSkillInfo(skill_id) {
          var getskillUrl =
            "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/" +
            skill_id;
          return new Promise((resolve, reject) => {
            axios
              .get(getskillUrl)
              .then((response) => {
                resolve(response);
              })
              .catch((err) => reject(err));
          });
        },
  
        getSkillRole(skill_id) {
          var getRoleSkillUrl =
            "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skillrolerelations/" +
            skill_id;
          return new Promise((resolve, reject) => {
            axios
              .get(getRoleSkillUrl)
              .then((response) => {
                resolve(response.data.data);
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
            this.$router.replace({ name: "skills" });
          }
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
        goBack() {
          this.$router.replace({ name: "skills" });
        },
      },
      async mounted() {
        document.title = "LJMS - Update skill";
        // get skill information from backend
        var skillInfo = await this.getSkillInfo(this.currentSkill_ID);
        var skillRoles = await this.getSkillRole(this.currentSkill_ID);
        
        skillInfo && skillRoles
          ? (this.noSkillFound = true)
          : (this.noSkillFound = false);
  
        // load data into the v-model and array
        this.skill_name.skill_name = skillInfo.data.data.Skill_Name;
        this.skill_description.skill_description =
        skillInfo.data.data.Skill_Description;
        this.roles_array = skillRoles;
        this.pillItemsFromComponent = skillRoles;
      },
    };
  </script>
  
  <style scoped>
    #updateSkillMain {
      min-height: 100vh;
    }
    .back-btn {
      border: none;
      background: none;
      line-height: 1;
      font-weight: 500;
      color: #113f7c;
      font-size: 18px;
    }
  
    .back-btn:hover {
      color: #404089;
      transition: 0.2s ease-in-out;
    }
  
    #submitBtn {
      background-color: #434ce8;
      color: #fbfbfb;
    }
  
    #submitBtn:hover {
      background-color: #404089;
      transition: 0.2s ease-in-out;
    }
  </style>
  