<template>
  <div>
    <div
      class="search-input"
      :class="this.autocompleteItems.length > 0 ? 'active' : ''"
    >
      <input
        type="text"
        :placeholder="this.placeholder"
        v-model="search"
        v-on:keyup="searchItem"
      />
      <div class="autocomplete-box">
        <li
          v-for="(value, key) in this.autocompleteItems"
          v-bind:key="key"
          @click="selectItem(value)"
        >
          {{ value[this.currName] }}
        </li>
      </div>
      <div class="icon">
        <i class="ph-magnifying-glass"></i>
      </div>
    </div>

    <div class="d-flex pills my-2">
      <div
        class="pill rounded-pill px-2 me-2 mt-2"
        v-for="(value, key) in this.pillItems"
        v-bind:key="key"
      >
        <div class="pill-content">
          <span class="pill-text p-2 px-1"> {{ value[this.currName] }} </span>
          <div class="pill-icon p-2 px-1 me-1">
            <i class="ph-x" @click="unselectItem(value[this.currID])"></i>
          </div>
        </div>
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
      currUrl: "",
      currName: "",
      currID: "",
      placeholder: "Search for " + this.ctype + "s to assign..."
    };
  },
  props: ["ctype", "skills", "roles"],
  methods: {
    searchItem() {
      // only search if the search bar is not empty
      if (this.search.length > 0 && this.items.length > 0) {
        this.autocompleteItems = this.items.filter((element) =>
          element[this.currName].toLowerCase().includes(this.search.toLowerCase())
        );
      } else if (this.search.length == 0) {
        this.autocompleteItems = [];
      }
    },

    selectItem(item) {
      if (this.pillItems.filter(currItem => currItem[this.currID] === item[this.currID]).length < 1)  {
        !this.pillItems.includes(item) ? this.pillItems.push(item) : null; // only push non duplicate items
      }
      this.search = "";
      this.autocompleteItems = [];
      this.$emit('pillItems', this.pillItems);  // emit the pillItems array to the parent component
    },

    unselectItem(item) {
      this.pillItems = this.pillItems.filter((value) => value[this.currID] != item); // remove item from pillItems array
      console.log(this.pillItems)
      this.$emit('pillItems', this.pillItems);  // emit the pillItems array to the parent component
    },

    // getRoleSkill(role_id) {
    //   var getRoleSkillUrl =
    //     "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roleskillrelations/" +
    //     role_id;
    //   return new Promise((resolve, reject) => {
    //     axios
    //       .get(getRoleSkillUrl)
    //       .then((response) => {
    //         resolve(response.data.data);
    //       })
    //       .catch((err) => reject(err));
    //   });
    // },
  },

  computed: {},

  async mounted() {
    if (this.ctype == 'skill') {
      this.currName = 'Skill_Name';
      this.currID = 'Skill_ID';
      this.currUrl = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/available/";
    } else if (this.ctype == 'role') {
      this.currName = 'Role_Name';
      this.currID = 'Role_ID';
      this.currUrl = "https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/available/";
    };
    axios.get(this.currUrl).then((response) => {
      var result = response.data.data;
      this.items = result;
    });

    // This is for update role page, to get the skills that are already assigned to the role
    if (this.skills) {
      this.pillItems = this.skills;
    }
  },
};
</script>
<style scoped>
  .search-input {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 5px;
    box-shadow: 0 1px 5px 3px rgba(114, 114, 114, 0.1);
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
    display: inline-flex;
    background-color: transparent;
    border: 1.5px solid #434ce8;
    color: #434ce8;
    line-height: 15px;
    font-weight: 800;
    min-width: max-content;
    text-align: center;
  }

  .pill-content {
    display: flex;
    /* font-size: 12px; */
    align-items: center; /* now its vertically centered */
  }

  .pill-icon {
    /*flex: 1; not necessary since you're using max-width*/
    max-width: 18px;
    /* padding: 10px 0 4px; */
    text-align: center; /* for horizontal alignment */
  }

  .ph-x {
    font-size: 18px;
    text-align: center;
    font-weight: 800;
    cursor: pointer;
  }

  .pill-text {
    font-size: 13px;
  }

  .pills {
    flex-wrap: wrap;
  }
</style>
