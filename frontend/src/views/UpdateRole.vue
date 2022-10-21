<template>
  <DashboardLayout>
    <div class="container-fluid p-sm-5" id="updateRoleMain">
      <!-- Spinner -->
      <div v-if="!noRoleFound" id="rippleP">
        <div class="lds-ripple">
          <div></div>
          <div></div>
        </div>
      </div>
      <div v-else
        class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body"
      >
        <h3>Update a Role</h3>
        <h6 class="text-secondary mt-3 mb-3">
          Change the existing values in the input box
        </h6>

        <!-- Popup -->
        <div v-show="checked">
          <ModalComponent
            type="Role"
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
            :role_id="this.$route.params.role_id"
            @pillItems="getPill"
          ></PillSearchComponent>
        </form>

        <!-- Buttons -->
        <div class="row d-flex justify-content-around my-sm-3 my-md-5 p-3">
          <button @click="goBack" type="button" class="btn col-md-4 col-sm-5 m-2 btn-secondary">
            Back
          </button>
          <button type="button" class="btn col-md-4 col-sm-5 m-2 btn-primary">
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

export default {
  name: "UpdateRole",
  components: {
    DashboardLayout,
    FormComponent,
    ModalComponent,
    PillSearchComponent,
    PillComponent,
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
      this.updateRole().then((res) => {
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
              if (this.RNerrors.includes(msg)) {
                this.role_name.errors.push(msg);
              } else {
                this.role_description.errors.push(msg);
              }
            }
          }
          // show Modal
          this.checked = true;
        });
      });
    },
    updateRole() {
      var createRoleUrl =
        "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/";
      return new Promise((resolve, reject) => {
        axios
          .post(createRoleUrl, {
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
        "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roleskillrelations/";
      return new Promise((resolve, reject) => {
        axios
          .post(assignSkillsUrl, {
            Role_ID: role_id,
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
        // Not done -- waiting for Siang to finish the backend amendments

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
    resetForm() {
      this.role_name.role_name = "";
      this.role_description.role_description = "";
    },
    onClickModal(value) {
      // modal is closed
      // reset checked value:
      this.checked = value;
      if (this.isSubmitted && this.isSuccess) {
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

      // submitted form
      this.isSubmitted = true;
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
    var role_id = this.$route.params.role_id;
    var roleInfo = await this.getRoleInfo(role_id);
    roleInfo ? (this.noRoleFound = true) : (this.noRoleFound = false);
    this.role_name.role_name = roleInfo.data.data.Role_Name;
    this.role_description.role_description = roleInfo.data.data.Role_Description;
  },
};
</script>

<style scoped>
  #updateRoleMain {
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
    z-index: 100;
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
