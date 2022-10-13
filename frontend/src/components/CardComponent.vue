<template>
  <div class="card-component mt-3 mb-3 mx-auto">
    <div class="row">

      <!-- Title -->
      <div class="card-component-header m-1 ps-3 col">
        <h5 class="card-component-title text-start">{{ title }}</h5>
      </div>

      <!-- Menu Button -->
      <div class="menu-frame col">
        <button class="menu-dot" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li><a class="dropdown-item" href="#">Update</a></li>
          <li><a class="dropdown-item" href="#">Delete</a></li>
        </ul>
      </div>

      <!-- Description -->
      <div class="card-component-body m-1 ps-3 ">
        <p class="card-component-text text-start pe-3">
          {{ desc }}
        </p>
      </div>

      <!-- Pill Buttons -->
      <div>

      </div>

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
  height: 160px;
  box-shadow: 0 3px 3px 0 rgb(0 0 0 / 4%), 0 5px 15px 0 rgb(0 0 0 / 4%);
}

.card-component-header {
  display: flex;
  justify-content: space-between;
  background-color: transparent;
  align-items: center;
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
}

.menu-frame {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  height: 20px;
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
