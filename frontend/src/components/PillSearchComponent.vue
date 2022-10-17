<template>
<div>
  <div
    class="search-input"
    :class="this.autocompleteItems.length > 0 ? 'active' : ''"
  >
    <input
      type="text"
      placeholder="Search for skills to assign.."
      v-model="search"
      v-on:keyup="searchItem"
    />
    <div class="autocomplete-box">
      <li
        v-for="(value, key) in this.autocompleteItems"
        v-bind:key="key"
        @click="selectItem(value)"
      >
        {{ value.Skill_Name }}
      </li>
    </div>
    <div class="icon">
      <i class="ph-magnifying-glass"></i>
    </div>
  </div>


    <div class="d-flex pills mt-3">
      <div class="pill rounded-pill px-2 me-2">
        <span class="pill-text">Skill Name #1 </span>
        <i class="ph-x"></i>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "PillSearchComponent",
  data() {
    return {
      items: [],
      autocompleteItems: [],
      pillItems: [],
      search: "",
      url: {
        skill:
          "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/available/",
        role: "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/available/",
      },
    };
  },
  props: ["ctype"],
  methods: {
    searchItem() {
      if (this.search.length > 0 && this.items.length > 0) {
        this.autocompleteItems = this.items.filter((element) =>
          element.Skill_Name.toLowerCase().includes(this.search.toLowerCase())
        );
      } else if (this.search.length == 0) {
        this.autocompleteItems = [];
      }
    },
    selectItem(item) {
    // only push non duplicate items
    !this.pillItems.includes(item) ? this.pillItems.push(item) : null;
    console.log(this.pillItems);
    },
  },
  computed: {},
  mounted() {
    var url = this.url[this.ctype];
    axios.get(url).then((response) => {
      var result = response.data.data;
      this.items = result;
    });
  },
};
</script>
<style scoped>
.search-input {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 5px;
  box-shadow: 0 1px 5px 3px rgba(0, 0, 0, 0.1);
}

.search-input input {
  height: 55px;
  width: 100%;
  border: none;
  border-radius: 5px;
  padding: 0 60px 0 20px;
  font-size: 18px;
  outline: none;
}

.search-input .icon {
  position: absolute;
  top: 0;
  right: 0;
  height: 55px;
  width: 55px;
  text-align: center;
  font-size: 25px;
  color: #000;
  line-height: 65px;
  font-weight: 800;
}

.search-input .autocomplete-box {
  max-height: 280px;
  padding: 0px;
  overflow-y: auto;
  z-index: 1;
  opacity: 0;
  pointer-events: none;
}

.search-input.active .autocomplete-box {
  padding: 10px 8px;
  opacity: 1;
  pointer-events: auto;
}


.search-input li {
  list-style: none;
  padding: 8px 12px;
  width: 100%;
  border-radius: 3px;
  cursor: pointer;
  display: none;
  transition: opacity 1s ease-out;
}

.search-input.active .autocomplete-box li {
  display: block;
}

.pill {
  position: relative;
  background-color: #0d6efd;
  color: white;
  height: 25px;
  font-size: 12px;
  min-width: max-content;
  text-align: center;
}

.pill .ph-x {
  text-align: center;
  line-height: 80px;
  font-weight: 800;
}

.pill-text {
  padding: 2em;
  font-size: 16px;
  line-height: 16px;
}

.pills {
  overflow: scroll;
  /* overflow: hidden; */
  -ms-overflow-style: none; /* Internet Explorer 10+ */
  scrollbar-width: none; /* Firefox */
}

.pills::-webkit-scrollbar {
  display: none; /* Safari and Chrome */
}
</style>
