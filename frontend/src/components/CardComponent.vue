<template>
  <div class="card-component mt-3 mb-2 mx-auto p-4">
    <div class="row justify-content-between">
      <!-- Title -->
      <div class="card-component-header m-0 col-lg-8 col-9">
        <h5 class="card-component-title text-start">{{ title }}</h5>
      </div>

      <!-- Menu Button -->
      <div class="menu-frame col-3 d-flex flex-wrap justify-content-center"  v-if="authenticated && (user.Role == 1)">
        <button class="ph-dots-three menu-dot mx-auto pt-0" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li><a class="dropdown-item" @click="updateItem(id, ctype)">Update</a></li>
          <li><a class="dropdown-item" @click="deleteItem(id, ctype)">Delete</a></li>
        </ul>
      </div>

      <!-- Description -->
      <div class="card-component-body m-1 ms-0 my-0 ">
        <p class="card-component-text text-start">
          {{ desc }}
        </p>
      </div>

      <!-- Pill Buttons -->
      <pill-component :pillList="pillList" :ctype="ctype"/>

    </div>
  </div>
</template>

<script>
import PillComponent from "@/components/PillComponent.vue";
import axios from "axios";
import { createToast } from 'mosha-vue-toastify';
import router from "../router";
import { mapGetters } from "vuex";

export default {
  name: "CardComponent",
  components: { PillComponent },
  props: ["title", "desc", "active", "pillList", "id", "ctype"],
  methods: {
    deleteItem(id, ctype) {
      var url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/delete/" +id;
      if(ctype == "skill") {
        axios.put(url, {
          headers: {
            'Content-Type': 'application/json'
        }}).then((response) => {
          var result = response.data.success
          if (result) {
            createToast('Skill deleted successfully!', {
              type: 'success',
              position: 'top-center',
              timeout: 3000,
              dismissible: true,
              pauseOnFocusLoss: true,
              pauseOnHover: true,
              closeOnClick: true,
              closeButton: true,
              icon: true,
              rtl: false,
            });

            this.$emit('reload');
  
          } else {
            createToast('Skill deletion failed!', {
              type: 'error',
              position: 'top-center',
              timeout: 3000,
              dismissible: true,
              pauseOnFocusLoss: true,
              pauseOnHover: true,
              closeOnClick: true,
              closeButton: true,
              icon: true,
              rtl: false,
            });
            this.$emit('reload');
          }
        });
      } else if (ctype == 'role') {
        url = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/delete/" +id;
        axios.put(url, {
          headers: {
            'Content-Type': 'application/json'
        }}).then((response) => {
          var result = response.data.success
          if (result) {
            createToast('Role deleted successfully!', {
              type: 'success',
              position: 'top-center',
              timeout: 3000,
              dismissible: true,
              pauseOnFocusLoss: true,
              pauseOnHover: true,
              closeOnClick: true,
              closeButton: true,
              icon: true,
              rtl: false,
            });

            this.$emit('reload');
  
          } else {
            createToast('Role deletion failed!', {
              type: 'error',
              position: 'top-center',
              timeout: 3000,
              dismissible: true,
              pauseOnFocusLoss: true,
              pauseOnHover: true,
              closeOnClick: true,
              closeButton: true,
              icon: true,
              rtl: false,
            });
            this.$emit('reload');
          }
        });
      }
    },
    updateItem(id, ctype) {
      if(ctype == "skill") {
        router.push({ name: 'UpdateSkill', params: { role_id: id } });
      } else if (ctype == 'role') {
        router.push({ name: 'update-role', params: { role_id: id } });
      } 
    }
  },
  computed: {
    ...mapGetters({
      user: "auth/user",
      authenticated: "auth/authenticated",
    }),
  },
};
</script>

<style scoped>
  * {
    margin: 0;
    /* padding: 0; */
    box-sizing: border-box;
    /* font-family: "Poppins", sans-serif; */
  }

  .card-component {
    background-color: white;
    border-radius: 15px;
    cursor: pointer;
    transition: 0.2s;
    height: 170px;
    /* min-height: 160px; */
    /* height: min-content; */
    box-shadow: 0 3px 3px 0 rgb(0 0 0 / 4%), 0 5px 15px 0 rgb(0 0 0 / 4%);
  }

  .card-component-header {
    display: flex;
    justify-content: space-between;
    background-color: transparent;
    align-items: center;
  }

  .card-component-title {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    word-wrap: break-word;
  }

  .card-component-body {
    font-size: 0.8em;
    max-height: 85px;
    overflow: hidden;
    display: block;
  }

  .card-component-text {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    word-wrap: break-word;
  }

  .menu-frame {
    height: 30px;
    max-width: 60px;
    border-radius: 20px;
    background-color: #fbfbfb;
  }

  .menu-frame:hover, .menu-frame:active {
    background-color: #404089;
    transition: 0.2s ease-in-out;
  }

  .menu-dot {
    font-size: 2.1rem;
    background-color: transparent;
    color: #404089;
    border: none;
  }

  .menu-dot:hover, .menu-dot:active {
    color: #fbfbfb;
    transition: 0.2s ease-in-out;
  }

  .dropdown-toggle::after {
    display: none !important;
  }

  .dropdown-item:active, .dropdown-item:active {
    background-color: #404089;
    color: #fbfbfb;
    transition: 0.2s;
  }

  /* browser width is small */
  @media screen and (min-width: 768px) {
    .card-component-text {
      -webkit-line-clamp: 2;
    }
  }

  @media screen and (max-width: 516px) {
    .card-component-text {
      -webkit-line-clamp: 2;
    }
  }
</style>
