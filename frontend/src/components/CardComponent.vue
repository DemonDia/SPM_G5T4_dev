<template>
  <div class="card-component mt-3 mb-3 mx-auto" v-if="active">
    <div class="menu-frame">
        <button class="menu-dot" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li><a class="dropdown-item" href="#">Update</a></li>
          <li><a class="dropdown-item" href="#">Delete</a></li>
        </ul>
     
    </div>
    <div class="card-component-header m-1 p-1">
      <h5 class="card-component-title">{{ title }}</h5>
    </div>
    <div class="card-component-body">
      <p class="card-component-text">
        {{ desc }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardComponent",
  props: ["title", "desc", "active"],
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.card-component {
  padding: 20px 16px;
  background-color: white;
  border-radius: 15px;
  cursor: pointer;
  transition: 0.2s;
}

.card-component-header {
  display: flex;
  justify-content: space-between;
  background-color: transparent;
  align-items: center;
}

.card-component-body {
  font-size: 0.8em;
  word-wrap: break-word;
}

.menu-frame {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  height: 40px;
  max-width: 60px;
  padding: 0 20px;
  margin-left: auto;
  margin-right: 8px;
  border-radius: 20px;
  background-color: rgb(238, 238, 238);
}

.menu-dot {
  background-color: #9b9ba5;
  box-shadow: -6px 0 0 0 #9b9ba5, 6px 0 0 0 #9b9ba5;
  width: 4px;
  height: 4px;
  border: 0;
  padding: 0;
  border-radius: 50%;
 
}

.dropdown-toggle::after {
    display: none !important;
}

</style>
