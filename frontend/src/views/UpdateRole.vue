<template>
  <DashboardLayout>
    <div class="container-fluid p-sm-5" id="updateRoleMain">
      <!-- Spinner -->
      <SpinnerComponent v-if="!noRoleFound" />
      
      <!-- Content -->
      <div
        v-else
        class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body"
      >
        <button @click="goBack" class="ph-arrow-left back-btn mb-3">
          Back
        </button>
        <h3>Update a Role</h3>
        <h6 class="text-secondary mt-3 mb-3">
          Change the existing values in the input box
        </h6>

        <!-- Popup -->
        <div v-show="checked">
          <ModalComponent
            type="Role"
            func="update"
            :isSuccess="isSuccess"
            @clicked="onClickModal"
          />
        </div>

        <!-- Content -->
        <form @submit.prevent="handleSubmit" method="POST">
          <FormComponent
            v-model="role_name.role_name"
            :label="role_name.label"
            type="text"
            :limit="role_name.limit"
            :errors="role_name.errors"
            :isSubmitted="isSubmitted"
            :formType="role_name.formType"
          />

          <FormComponent
            v-model="role_description.role_description"
            :label="role_description.label"
            type="text"
            :limit="role_description.limit"
            :errors="role_description.errors"
            :isSubmitted="isSubmitted"
            :formType="role_description.formType"
          />

          <PillSearchComponent
            class="mt-3"
            ctype="skill"
            :skills="skills_array"
            @pillItems="getPill"
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
            Update Role
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
    name: "UpdateRole",
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
        role_name: {
          role_name: "",
          label: "Role Name",
          limit: "30",
          errors: [],
          formType: "input",
        },
        role_description: {
          role_description: "",
          label: "Role Description",
          limit: "170",
          errors: [],
          formType: "textarea",
        },
        isSuccess: false,
        isSubmitted: false,
        checked: false,
        RNerrors: [
          "Role Name cannot be empty! Please try again",
          "Role already exists! Please try again",
          "Role Name exceeds character limit of 30! Please try again",
        ],
        pillItemsFromComponent: [],
        noRoleFound: false,
        skills_array: [],
        currentRole_ID: this.$route.params.role_id,
      };
    },
    methods: {
      // Logic
      // To collect all the information from the model and send it to the backend

      // Steps
      // View Role will pass the role_id to this page
      // This page will use the role_id to get the role information from the backend
      // The role information will be displayed in the input boxes
      // The user can change the information and submit it to the backend
      // The backend will update the role information in the database
      // The user will be redirected to the View Role page

      handleSubmit() {
        // submitted form
        this.isSubmitted = true;
        this.updateRole(this.currentRole_ID).then((res) => {
          var roleStatus = res.data;
          // check success
          if (roleStatus.success) {
            this.assignSkills(this.currentRole_ID).then((result) => {
              this.resetErrors();
              // this.resetForm();
              this.isSuccess = true;
              this.checked = true; // show Modal
            });
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
            this.checked = true; // show Modal
          }
        });
      },

      updateRole(role_id) {
        var updateRoleUrl =
          "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/" +
          role_id;
        return new Promise((resolve, reject) => {
          axios
            .put(updateRoleUrl, {
              Role_Name: this.role_name.role_name,
              Role_Description: this.role_description.role_description,
              Active: true,
            })
            .then((response) => {
              resolve(response);
            })
            .catch((err) => reject(err));
        });
      },

      assignSkills(role_id) {
        var assignSkillsUrl =
          "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roleskillrelations/" +
          role_id;
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

      getRoleSkill(role_id) {
        var getRoleSkillUrl =
          "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roleskillrelations/" +
          role_id;
        return new Promise((resolve, reject) => {
          axios
            .get(getRoleSkillUrl)
            .then((response) => {
              resolve(response.data.data);
            })
            .catch((err) => reject(err));
        });
      },

      // resetForm() {
      //   this.role_name.role_name = "";
      //   this.role_description.role_description = "";
      // },

      onClickModal(value) {
        // modal is closed
        // reset checked value:
        this.checked = value;
        if (this.isSuccess) {
          // go back to View All
          this.$router.replace({ name: "roles" });
        }
      },

      getPill(item) {
        // emit content to be passed into the pillItemsFromComponent
        this.pillItemsFromComponent = item;
      },

      resetErrors() {
        // reset fields
        this.role_name.errors = [];
        this.role_description.errors = [];
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
        this.$router.replace({ name: "roles" });
      },
    },
    async mounted() {
      document.title = "LJMS - Update Role";
      // get role information from backend
      var roleInfo = await this.getRoleInfo(this.currentRole_ID);
      var roleSkills = await this.getRoleSkill(this.currentRole_ID);
      roleInfo && roleSkills
        ? (this.noRoleFound = true)
        : (this.noRoleFound = false);

      // load data into the v-model and array
      this.role_name.role_name = roleInfo.data.data.Role_Name;
      this.role_description.role_description =
      roleInfo.data.data.Role_Description;
      this.skills_array = roleSkills;
      this.pillItemsFromComponent = roleSkills;
    },
  };
</script>

<style scoped>
  #updateRoleMain {
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
