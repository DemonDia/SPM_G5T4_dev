<template>
  <DashboardLayout>
    <div class="container-fluid p-5" id="createRoleMain">
      <div class="w-50 h-75 mx-auto p-5 text-start rounded rounded-4 shadow-lg p-3 mb-5 bg-body">
        <h2>Create a role</h2>
        <h4>efgegeg</h4>

        <div v-show="this.currFormPg==1" id="formPg1">
          page1
        </div>
        <div v-show="this.currFormPg==2" id="formPg2">
          page2
        </div>
        <div v-show="this.currFormPg==3" id="formPg3">
          page3
        </div>
        
        <nav aria-label="Page navigation example">
          <ul class="pagination justify-content-center">
            <li class="page-item" :class="this.currFormPg == 1 ? 'disabled' : ''">
              <a class="page-link" href="#" tabindex="-1" @click="goToPrevPg">
                Previous
              </a>
            </li>
            <li class="page-item" :class="this.currFormPg==1 ? 'active' : ''">
              <a class="page-link" href="#formPg1" @click="goToPg(1)">
                1
              </a>
            </li>
            <li class="page-item" :class="this.currFormPg==2 ? 'active' : ''">
              <a class="page-link" href="#formPg2" @click="goToPg(2)">
                2
              </a>
            </li>
            <li class="page-item" :class="this.currFormPg==3 ? 'active' : ''">
              <a class="page-link" href="#formPg3" @click="goToPg(3)">
                3
              </a>
            </li>
            <li class="page-item" :class="this.currFormPg == 3 ? 'disabled' : ''">
              <a class="page-link" href="#" @click="goToNextPg">
                Next
              </a>
            </li>
          </ul>
        </nav>
  
        <!-- <div v-show="checked">
          <ModalComponent type="Role" :isSuccess="isSuccess" @clicked="onClickModal"/>
        </div>
  
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
        </form> -->
      </div>
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
        ],
        currFormPg: 1,
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
      },
      goToPrevPg() {
        this.currFormPg -= 1
      },
      goToNextPg() {
        this.currFormPg += 1
      },
      goToPg(x) {
        this.currFormPg = x
      }
    },
    mounted() {
      document.title = "LJMS - Create Roles";
    },
  };
</script>

<style scoped>

  #createRoleMain {
    height: 100vh;
  }
  
</style>
