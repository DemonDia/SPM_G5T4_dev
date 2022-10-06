<template>
    <DashboardLayout>
      <div class="container-fluid p-5" id="createSkillMain">
        <h1>Create a skill</h1>
  
        <div v-show="checked">
          <ModalComponent type="Role" :isSuccess="isSuccess" @clicked="onClickModal"/>
        </div>
  
  
        <form @submit.prevent="createSkill" method="POST">
          <FormComponent
            v-model="SkillName.SkillName"
            :label="SkillName.label"
            type="text"
            :limit="SkillName.limit"
            :errors="SkillName.errors"
            :isSubmitted="isSubmitted"
          /> 
          <FormComponent
            v-model="SkillDescription.SkillDescription"
            :label="SkillDescription.label"
            type="text"
            :limit="SkillDescription.limit"
            :errors="SkillDescription.errors"
            :isSubmitted="isSubmitted"
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
      name: "CreateSkill",
      components: {
        DashboardLayout,
        FormComponent,
        ModalComponent,
      },
      data() {
        return {
          SkillName: {
            SkillName: "",
            label: "Skill Name",
            limit: "30",
            errors: [],
          },
          SkillDescription: {
            SkillDescription: "",
            label: "Skill Description",
            limit: "170",
            errors: [],
          },
          isSuccess: false,
          isSubmitted: false,
          checked: false,
          RNerrors: [
            "Skill name cannot be empty! Please try again",
            "Skill already exists! Please try again",
            "Skill name exceeds character limit of 30! Please try again"
          ]
        };
      },
      methods: {
        createSkill() {
          // === LINKING FRONT TO BACKEND ===
          var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/"

          axios
            .post(url, {
              "SkillName": this.SkillName.SkillName,
              "SkillDescription": this.SkillDescription.SkillDescription,
              "Active": true
            })
            .then((response) => {

            console.log(response);
              // reset fields
              this.SkillName.errors = []
              this.SkillDescription.errors = []
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
                    this.SkillName.errors.push(msg)
                  }
                  else {
                    this.SkillDescription.errors.push(msg)
                  }
                }
              }
              // show Modal
              this.checked = true;
            });
            this.resetForm()
        },
        resetForm() {
          this.SkillName.SkillName = "";
          this.SkillDescription.SkillDescription = "";
        },
        onClickModal(value) {
          // console.log("got value from Modal")
          // console.log(value)
  
          // reset checked value:
          this.checked = value;
        }
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
    
  </style>
  