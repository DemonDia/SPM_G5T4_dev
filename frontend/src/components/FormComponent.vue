<template>
  <div class="row d-flex justify-content-center m-5 ms-0">
    <div class="col-3 text-end pt-1">
        <label class="form-label" v-if="label">
          {{ label }}
        </label>
    </div>
    <div class="col-sm-4">
      <div>
        <input
          v-bind="$attrs"
          :value="modelValue"
          :placeholder="label"
          @input="$emit('update:modelValue', $event.target.value)"
          v-on:keyup="this.checkChar"
          class="form-control"
        >
      </div>
      <p v-if="this.overLimit" class="p-2 text-start text-danger">
        {{this.error}}
      </p>
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
      },
      limit: {
        type: String,
        default: ''
      }
    },
    data() {
      return {
        error: "",
        overLimit: true,
      }
    },
    methods: {
      checkChar(){
        if (this.modelValue.length > Number(this.limit)) {
          var excess = this.modelValue.length - Number(this.limit)
          this.error = "You are " + excess + " character(s) over the limit!"
          this.overLimit = true
        }
        else {
          if (this.overLimit == true) {
            this.overLimit = !this.overLimit
          }
        }
      }
    }
  }
</script>
<style scoped>
  
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
  }
 
</style>