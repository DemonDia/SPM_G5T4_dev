<template>
  <div class="card-component m-3 p-3">
    <div class="row justify-content-between">
      <div class="col-md-3 col-12 m-1 p-3 mx-auto">
        <img :src="`https://picsum.photos/id/${this.indx}/200/200`" class="img-fluid" alt=""/>
      </div>

      <div class="col-6 flex-grow-1 card-content p-2 px-4 pt-0">
        <h5 class="card-title text-start m-1 pt-3 pb-0">{{ this.title }}</h5>
        <div class="card-body m-1">
          <p class="card-text text-start">
            {{ this.desc }}
          </p>
        </div>
        <div class="card-bottom">
          <pill-component :pillList="this.skills" ctype="role"/>
        </div>
      </div>

      <div class="col-1 menu-frame d-flex flex-wrap">
        <button
              class="ph-dots-three-vertical menu-dot"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
        ></button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li><a class="dropdown-item" href="#">Update</a></li>
          <li><a class="dropdown-item" href="#">Delete</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import PillComponent from "./PillComponent.vue";

export default {
  name: "CourseComponent",
  components: {
    PillComponent
  },
  props: ["course", "indx"],
  data() {
    return {
      category: this.course.Course_Category,
      desc: this.course.Course_Desc,
      courseId: this.course.Course_ID,
      title: this.course.Course_Name,
      status: this.course.Course_Status,
      type: this.course.Course_Type,
      skills: this.course.Skills,
    }
  },
  methods: {

  },
  mounted() {
    console.log(this.course);
  }
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
    height: 30px;
    max-width: 60px;
    padding: 0 20px; 
    margin-left: auto;
    margin-right: 8px;
    border-radius: 20px;
  }

  .menu-dot {
    font-size: 2.1rem;
    background-color: transparent;
    border: none;
  }
</style>
