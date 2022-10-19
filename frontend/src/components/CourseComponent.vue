<template>
  <div class="card-component mt-3 mb-2 mx-auto p-3 ps-4">
    <div class="row">
      <!-- Image -->
      <img src="https://picsum.photos/600" alt="" />

      <!-- Title -->
      <div class="card-content">
        <h4 class="card-title">{{ title }}</h4>
        
        <!-- Description -->
        <p class="card-description">
          {{ desc }}
        </p>
        <div class="card-bottom">
          <div class="options">
            <!-- Pills Component -->
            <p class="fw-bold">Skills</p>
            <pill-component class="mt-3" :pillList="pillList" :ctype="ctype"/>
          </div>
        </div>
      </div>

      <!-- Menu Button -->
      <div class="menu-frame col-3 mt-0 p-3 pt-0">
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
  name: "CardComponent",
  components: {
    PillComponent
  },
  props: ["title", "desc", "active" ,"pillList", "ctype"],
  methods: {},
};
</script>

<style scoped>
* {
  margin: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

img {
  border-radius: 10%;
  display: block;
  object-fit: cover;
  margin: 0 auto;
  max-width: 15%;
  min-height: 100%;
  transition: all 0.5s ease 0s;
}

.card-component {
  padding: 20px 16px;
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
  padding: 0.8rem;
}
.card-title {
  text-align: left;
	font-size: 1.2rem;
  font-weight: 700;
  margin: 0;
}

.card-description {
  text-align: left;
	font-size: 0.8rem;
  margin: 0;
  margin-top: 1rem;
  color: #888;
	overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  max-height: 2rem;
  line-height: 1rem;
}
.card-bottom {
	display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
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
  text-align: center;
  font-weight: 700;
  font-size: 1rem;
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
