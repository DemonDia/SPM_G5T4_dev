<template>
  <DashboardLayout>
    <div class="container-fluid p-5" id="createRoleMain">
      <div class="col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body">
        <h3>Create a Role</h3>
        <h5>What role would you like to create today?</h5>
        
        <!-- <div v-show="checked">
          <ModalComponent type="Role" :isSuccess="isSuccess" @clicked="onClickModal"/>
        </div> -->

        <!-- Progress Tracker -->
        <div class="row gx-4 progress p-0">
          <div class="col-12 col-md-4" v-for="(value,key) in progress" :key="key">
            <div class="row">
              <div class="progressbar mb-3" :style="[this.currFormPg > key ? {'background-color': value.bg} : {'background-color': '#404089', 'opacity': 0.1}]">
            </div>
            <div class="row">
              <p class="mb-0 fw-bold" :style="[this.currFormPg > key ? {'color': 'black'} : {'opacity': 0.4}]">
                {{value.title}}
              </p>
            </div>
            <div class="row">
              <p :style="[this.currFormPg > key ? {'color': 'black'} : {'opacity': 0.4}]">
                {{value.description}}
              </p>
            </div>
            </div>
          </div>
        </div>

        <form @submit.prevent="createRole" method="POST">
        <!-- Content -->
        <div v-show="this.currFormPg==1" id="formPg1">
          
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

        </div>
        <div v-show="this.currFormPg==2" id="formPg2">
          page2
        </div>
        <div v-show="this.currFormPg==3" id="formPg3">
          page3
        </div>
        </form>
        
        <div class="row d-flex justify-content-around my-5 p-3">
          <button type="button" class="btn col-md-4 col-sm-6 m-2" 
            :class="this.currFormPg == 1 ? 'btn-outline-secondary disabled' : 'btn-primary'" 
            @click="goToPrevPg"
          >
            {{this.progress[currFormPg-1].button1}}
          </button>
  
          <button type="button" class="btn col-md-4 col-sm-5 m-2"  
            :class="this.currFormPg == 3 ? 'btn-warning' : 'btn-primary'" 
            @click="goToNextPg"
          >
          {{this.progress[currFormPg-1].button2}}
          </button>
        </div>

        <!-- <div class="alert alert-danger" v-if="errors.length">
          <b>Please correct the following error(s):</b>
          <ul>
            <li v-for="(error, index) in errors" v-bind:key="index">
              {{ error }}
            </li>
          </ul>
        </div> -->

        <!-- 
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
  import BoxComponent from "../components/BoxComponent.vue";

  export default {
    name: "CreateRole",
    components: {
      DashboardLayout,
      FormComponent,
      ModalComponent,
      BoxComponent
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
        progress: [
          {
            'title': 'STEP 1',
            'bg': '#56d1dc',
            'description': 'Input Role details',
            'button1': 'Back to Step 1',
            'button2': 'Next: Assign Skills',
          },
          {
            'title': 'STEP 2',
            'bg': '#5d7bd5',
            'description': 'Assign skills (optional)',
            'button1': 'Back to Step 1',
            'button2': 'Next: Confirm summary',
          }, 
          {
            'title': 'STEP 3',
            'bg': '#404089',
            'description': 'Confirm summary',
            'button1': 'Back to Step 2',
            'button2': 'Submit',
          },
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
        // reset checked value:
        this.checked = value;
      },
      goToPrevPg() {
        this.currFormPg -= 1
      },
      goToNextPg() {
        this.currFormPg += 1
      },goToPg(x) {
        this.currFormPg = x
      },
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

  .progress{
    height: fit-content;
    background-color: whitesmoke;
    font-size: 15px;
    margin: 5px 0;
  }
  
  .progressbar {
    border-radius: 2px;
    height: 8px;
  }

</style>
