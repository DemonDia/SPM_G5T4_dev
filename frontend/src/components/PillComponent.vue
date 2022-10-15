<template>
  <div class="m-1 mb-0 px-3">
    <p class="text-start fw-bold pill-text mb-1">
      Skills required:
    </p>
    <div class="d-flex pills">
      <div v-for="(value, key) in pillList" v-bind:key="key" class="pill rounded-pill px-2 me-2">
        <p> {{ value }} </p>
      </div>
    </div>
  </div>
</template>
  
<script>
  export default {
    name: "PillComponent",
    data() {
      return {
      }
    },
    props: ['pillList'],
    methods: {
      
    },
    computed: {
    }
  }
</script>
<style scoped>
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