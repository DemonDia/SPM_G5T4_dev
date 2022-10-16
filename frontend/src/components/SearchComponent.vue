<template>
    <div class="search-container mt-3">
        <i class="ph-magnifying-glass"></i>
        <input type="text" name="" id="" class="side-search" placeholder="Skill title or keyword"/>
        <div class="vl"></div>
        <i class="ph-briefcase"></i>
        <input type="text" name="" id="" class="main-search" placeholder="Add Role or anything">
        <input type="button" class="search-button" value="Search">
    </div>
  </template>
  
  <script>
  export default {
    name: "SearchComponent",
    data() {
      return {};
    },
  };
  </script>
  
  <style scoped>

  * {
    font-family: "Poppins", sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }


  input[type="text"] {
    width: 100%;
    height: 30px;
    border: 0;
    padding: 0 10px;
    font-size: 16px;
    outline: none;
  }

  .search-container {
    background: #fff;
    display: flex;
    align-items: center;
    font-size: 20px;
    max-width: 50em;
    height: 4em;
    margin: auto;
    padding: 1.3em 1em;
    border-radius: 3em;
  }

  .vl {
  border-left: 1px solid rgb(215, 215, 215);
  height: 2em;
  margin: 0 1em;
  
 }

 .side-search {
    width: 50% !important;
 }

 .search-button {
    background: #fff;
    border: 1px solid rgb(215, 215, 215);
    border-radius: 3em;
    color: #000;
    font-size: 16px;
    font-weight: 600;
    height: 3em;
    margin-left: 1em;
    padding: 0 1.5em;
    text-transform: uppercase;
    transition: 0.3s;
    cursor: pointer;
    outline: none;
  }

  .search-button:hover {
    background: #000;
    color: #fff;
  }

  .main-search {
    width: 100% !important;
  }

  .ph-magnifying-glass {
    color: #000;
    font-size: 1.5em;
    margin-right: 0.5em;
  }

  .ph-briefcase {
    color: #000;
    font-size: 1.5em;
    margin-right: 0.5em;
  }

  </style>
  