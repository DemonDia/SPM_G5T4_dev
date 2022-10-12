<template>
  <DashboardLayout>
    <div class="container-fluid p-5" id="createRoleMain">
      <h1>Create a role</h1>

      <div v-show="checked">
        <ModalComponent type="Role" :isSuccess="isSuccess" @clicked="onClickModal"/>
      </div>

      <!-- <div class="alert alert-danger" v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="(error, index) in errors" v-bind:key="index">
            {{ error }}
          </li>
        </ul>
      </div> -->

      <form @submit.prevent="createRole" method="POST">
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
        <button class="btn btn-secondary m-3" @click="resetForm" type="reset">
          Reset
        </button>
        <button class="btn btn-primary" type="submit" data-bs-toggle="modal" data-bs-target="#submitModal">
          Submit
        </button>
      </form>
    </div>
  </DashboardLayout>
</template>

<script>
  import DashboardLayout from "./Dashboard/Layout/DashboardLayout.vue";
  import FormComponent from "../components/FormComponent.vue";
  import ModalComponent from "../components/ModalComponent.vue";
  import axios from "axios";

  export default {
    name: "CreateRole",
    components: {
      DashboardLayout,
      FormComponent,
      ModalComponent,
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
          "Role Name exceeds character limit of 30! Please try again"
        ]
      };
    },
    methods: {
      createRole() {
        // === LINKING FRONT TO BACKEND ===
        var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/"
        axios
          .post(url, {
            "Role_Name": this.role_name.role_name,
            "Role_Description": this.role_description.role_description,
            "Active": true
          })
          .then((response) => {
            // reset fields
            this.role_name.errors = []
            this.role_description.errors = []
            this.isSubmitted = NaN

            // submitted form
            this.isSubmitted = true;

            // console.log(response.data);
            if (response.data.success) {
              // console.log("success")
              // success case
              this.isSuccess = true;
            } 
            else {
              // console.log("failure")
              this.isSuccess = false;
              for (let err in response.data.message) {
                let msg = response.data.message[err]
                if (this.RNerrors.includes(msg)) {
                  this.role_name.errors.push(msg)
                }
                else {
                  this.role_description.errors.push(msg)
                }
              }
            }
            // show Modal
            this.checked = true;
          });
          this.resetForm()
      },
      resetForm() {
        this.role_name.role_name = "";
        this.role_description.role_description = "";
      },
      onClickModal(value) {
        // console.log("got value from Modal")
        // console.log(value)

        // reset checked value:
        this.checked = value;
      }
    },
    mounted() {
      document.title = "LJMS - Create Roles";
    },
  };
</script>

<style scoped>

  #createRoleMain {
    min-height: 100vh;
  }
  
</style>
