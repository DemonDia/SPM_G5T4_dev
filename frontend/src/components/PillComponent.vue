<template>
  <div class="m-1">
    <p class="text-start fw-bold pill-text mb-1" v-if="ctype=='role'">
      Required Skills:
    </p>
    <p class="text-start fw-bold pill-text mb-1" v-if="ctype=='skill'">
      Related Roles:
    </p>
    <div class="d-flex pills">
      <div v-for="(value, key) in pillList" v-bind:key="key" class="pill rounded-pill px-2 me-1 mb-1">
        <p> {{ value }} </p>
      </div>
      <div v-if="pillList.length==0" class="pill rounded-pill px-2 mb-1 me-1">
        <p> None </p>
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
    props: ['pillList' ,'ctype'],
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
    height: 18px;
    font-size: 13px;
    min-width: max-content;
    text-align: center;
  }

  .pill-text {
    font-size: 12px;
  }

  .pills {
    overflow-y: scroll;
    /* overflow: hidden; */
    -ms-overflow-style: none;  /* Internet Explorer 10+ */
    scrollbar-width: none;  /* Firefox */
  }

  .pills::-webkit-scrollbar { 
    display: none;  /* Safari and Chrome */
  }

</style>