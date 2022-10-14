<template>
  <div v-for="(value, key) in pillList" v-bind:key="key" class="pill rounded-pill px-2 me-2" >
    <p> {{ value }} </p>
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
      
    }
  }
</script>
<style scoped>
  .pill {
    background-color: #0d6efd;
    color: white;
    width: fit-content;
    height: 17px;
    font-size: 12px;
  }
 
</style>