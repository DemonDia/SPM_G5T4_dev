<template>
  <div class="card-component container-fluid m-4 mx-auto py-4 ps-4">
    <div class="justify-content-between d-flex flex-wrap">
      <!-- Image -->
      <div class="col-lg-4 col-sm-12 mx-auto my-2">
        <img :src="`https://picsum.photos/id/${this.indx}/200/200`" class="img-fluid" alt=""/>
      </div>
      
      <div class="col-lg-7 col-md-11 card-content my-2 py-3 pt-1 mt-0">
        <!-- Title -->
        <h4 class="card-title text-start text-break">{{ this.title }}</h4>
        <!-- Description -->
        <p class="card-description text-start text-break my-2">
          {{ this.desc }}
        </p>
        <!-- Skills -->
        <div class="card-bottom flex-wrap">
          <!-- <div class="options"> -->
            <!-- Pills Component -->
            <!-- <p class="fw-bold">Skills</p> -->
            <pill-component :pillList="this.skills" ctype="role"/>
          <!-- </div> -->
        </div>
      </div>
      <div class="col-1 order-1">
        <!-- Menu Button -->
        <div class="menu-frame mt-0 p-3 pt-0">
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
  </div>
</template>

<script>
import PillComponent from "./PillComponent.vue";

export default {
  name: "CardComponent",
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
  font-family: "Poppins", sans-serif;
  /* overflow: hidden; */
}

img {
  border-radius: 10%;
  display: block;
  object-fit: cover;
  margin: 0 auto;
  /* max-width: 15; */
  /* min-height: 100%; */
  transition: all 0.5s ease 0s;
}

.card-component {
  /* padding: 20px 16px; */
  background-color: white;
  border-radius: 15px;
  cursor: pointer;
  transition: 0.2s;
  max-height: 30%;
  box-shadow: 0 3px 3px 0 rgb(0 0 0 / 4%), 0 5px 15px 0 rgb(0 0 0 / 4%);
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
  display: flex;
  flex-wrap: wrap;
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

.dropdown-toggle::after {
  display: none !important;
}

.card-content {
  flex: 1 50%;
  -webkit-flex: 1 50%;
}
.card-title {
	font-size: 1.2rem;
  font-weight: 700;
}

.card-description {
	font-size: 0.8rem;
  color: #888;
  line-height: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  word-wrap: break-word;
}

.card-bottom {
	display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  overflow: hidden;
	align-content: center;
	-webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
	border-top: 1px solid #efefef;
  text-align: right;
	padding-top: 0.5rem;
	margin-top: 1rem;
	font-size: 0.8rem;
  text-align: left;
	color: rgb(0, 0, 0);
}

.card__price {
  color: #E35354;
  font-weight: 700;
  font-size: 1rem;
}


/* browser width is small */
@media screen and (max-width: 991px) {
  .card-component-text {
    -webkit-line-clamp: 3;
  }
}
</style>
