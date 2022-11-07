<template>
  <div v-if="this.status=='Active'" class="card-component m-4 p-3">
    <div class="row justify-content-between">
      <!-- Image -->
      <div class="col-md-3 col-12 p-3 mx-auto">
        <img :src="`https://picsum.photos/id/${this.indx}/200/200`" class="img-fluid" alt="Course Image Illustration"/>
      </div>

      <!-- Card Content -->
      <div class="col-6 flex-grow-1 card-content p-2 px-4 pt-0 pt-md-2">
        <div class="tags text-start p-2 ps-0 mt-0 my-2">
          <span class="badge text-dark me-2" id="typeBadge">
            <p>{{ this.type }}</p>
          </span>
          <span class="badge text-dark me-2" id="catBadge">
            <p>{{ this.category }}</p>
          </span>
        </div>
        <h5 class="card-title text-start my-2">
          {{ this.courseID + ": " + this.title }}
        </h5>
        <div class="card-body my-2">
          <p class="card-text text-start">{{ this.desc }}</p>
        </div>
        <div class="card-bottom my-2">
          <pill-component :pillList="this.skills" ctype="role"/>
        </div>
      </div>

      <!-- Menu Button -->
      <div class="col-1 menu-frame d-flex flex-wrap" v-if="authenticated && (user.Role == 1)">
        <button
              class="ph-dots-three-vertical menu-dot"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
        ></button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li><a class="dropdown-item" @click="updateItem(this.courseID,'course')">Update</a></li>
          <!-- <li><a class="dropdown-item" href="#">Delete</a></li> -->
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import PillComponent from "@/components/PillComponent.vue";
import router from "../router";
import { mapGetters } from "vuex";

export default {
  name: "CourseComponent",
  components: {
    PillComponent
  },
  props: ["course", "indx", "id", "ctype"],
  data() {
    return {
      category: this.course.Course_Category,
      desc: this.course.Course_Desc,
      courseID: this.course.Course_ID.toUpperCase(),
      title: this.course.Course_Name,
      status: this.course.Course_Status,
      type: this.course.Course_Type,
      skills: this.course.Skills,
    }
  },
  computed: {
    ...mapGetters({
      user: "auth/user",
      authenticated: "auth/authenticated",
    }),
  },
  methods: {
    updateItem(id, ctype) {
      if(ctype == "course") {
        router.push({ name: 'update-course', params: { course_id: id } });
      } 
    }
  },
};
</script>

<style scoped>
  * {
    margin: 0;
    box-sizing: border-box;
  }

  .card-component {
    background-color: white;
    border-radius: 15px;
    cursor: pointer;
    transition: 0.2s;
    height: max-content;
    box-shadow: 0 3px 3px 0 rgb(0 0 0 / 4%), 0 5px 15px 0 rgb(0 0 0 / 4%);
  }

  .card-component-header {
    display: flex;
    justify-content: space-between;
    background-color: transparent;
    align-items: center;
  }

  .card-title {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    word-wrap: break-word;
  }

  .card-body {
    max-height: 85px;
    overflow: hidden;
    display: block;
  }

  .card-text {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    word-wrap: break-word;
  }

  .menu-frame {
    justify-content: center;
    align-items: center;
    height: 32px;
    max-width: 60px;
    padding: 0 20px; 
    margin-left: auto;
    margin-right: 8px;
    border-radius: 20px;
  }

  .menu-frame:hover, .menu-frame:active {
    background-color: #404089;
    transition: 0.2s ease-in-out;
  }

  .menu-dot {
    font-size: 2rem;
    background-color: transparent;
    border: none;
  }

  .menu-dot:hover, .menu-dot:active {
    color: #fbfbfb;
    transition: 0.2s ease-in-out;
  }

  .dropdown-item:active, .dropdown-item:active {
    background-color: #404089;
    color: #fbfbfb;
    transition: 0.2s;
  }

  #typeBadge {
    border: 2px solid #3e0b5e;
    color: #3e0b5e;
  }

  #catBadge {
    border: 2px solid #b43e8f;
    color: #b43e8f;
  }
</style>
