<template>
<div class="row d-flex justify-content-center m-5">
    <div class="col-auto">
        <label class="form-label" v-if="label">{{ label }}</label>
    </div>
    <div class="col-sm-4">
        <input
        v-bind="$attrs"
        :value="modelValue"
        :placeholder="label"
        @input="$emit('update:modelValue', $event.target.value)"
        class="form-control"
        >
    </div>
</div>
  </template>
  
  <script>
  export default {
    props: {
      label: {
        type: String,
        default: ''
      },
      modelValue: {
        type: [String, Number],
        default: ''
      }
    }
  }
  </script>
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");
  
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
  }
 
  </style>
  