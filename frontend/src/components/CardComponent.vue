<template>
  <div class="cards-component">
    <div class="card-component col-3">
      <div class="menu-frame">
        <div class="menu-dot"></div>
      </div>
      <div class="card-component-header">
        <h5 class="card-component-title">{{ title }}</h5>
      </div>
      <div class="card-component-body">
        <p class="card-component-text">
          {{ desc }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'CardComponent', 
    props: ['title', 'desc']
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

.cards-component {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  max-width: 1200px;
  padding: 0 20px;
}

.card-component {
  padding: 20px 16px;
  /* background-color: rgb(243, 243, 243); */
  border-radius: 10px;
  cursor: pointer;
  transition: 0.2s;
}

.card-component-header {
  display: flex;
  justify-content: space-between;
  background-color: transparent;
  align-items: center;
  margin-bottom: 16px;
}

.card-component-body {
  font-size: 0.8em;
  word-wrap: break-word;
}

/* .menu-frame {
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
} */

.menu-dot {
  background-color: #9b9ba5;
  box-shadow: -6px 0 0 0 #9b9ba5, 6px 0 0 0 #9b9ba5;
  width: 4px;
  height: 4px;
  border: 0;
  padding: 0;
  border-radius: 50%;
  margin-left: auto;
  margin-right: 8px;
}
</style>
