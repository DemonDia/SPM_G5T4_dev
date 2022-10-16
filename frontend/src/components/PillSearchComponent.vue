<template>
    <div class="search-input">
        <input type="text" placeholder="Search for skills to assign.." v-model="search" v-on:keyup="searchItem">
        <div class="autocomplete-box">
            <li>Hi</li>
        </div>
        <div class="icon">
            <i class="ph-magnifying-glass"></i>
        </div>
    </div>
</template>
    
  <script>
    import axios from 'axios';

    export default {
      name: "PillSearchComponent",
      data() {
        return {
            items: [],
            search: '',
            url: {
                skill: 'https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/skills/available/',
                role: 'https://01p0cxotkg.execute-api.us-east-1.amazonaws.com/dev/roles/available/'
            }
        }
      },
      props: ['ctype'],
      methods: {
        searchItem() {
          console.log(this.filteredItems);
        },
      },
      computed: {
        filteredItems() {
          return this.items.filter(item => {
            return item.toLowerCase().includes(this.search.toLowerCase())
          })
        }
      }, 
      mounted() {
        var url = this.url[this.ctype];
        axios.get(url).then((response) => {
          var result = response.data.data
          this.items = result
          console.log(this.items)
        });
      },
    }
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
        /* padding: 10px 8px; */
        overflow-y: auto;
        z-index: 1;
        opacity: 0;
        pointer-events: none;
    }

    .search-input li {
        list-style: none;
        padding: 8px 12px;
        width: 100%;
        border-radius: 3px;
        cursor: pointer;
        display: none;
    }

    .pill {
      background-color: #0d6efd;
      color: white;
      height: 17px;
      font-size: 12px;
      min-width: max-content;
      text-align: center;
    }
  
    .pill-text {
      font-size: 12px;
    }
  
    .pills {
      overflow: scroll;
      /* overflow: hidden; */
      -ms-overflow-style: none;  /* Internet Explorer 10+ */
      scrollbar-width: none;  /* Firefox */
    }
  
    .pills::-webkit-scrollbar { 
      display: none;  /* Safari and Chrome */
    }
  
  </style>