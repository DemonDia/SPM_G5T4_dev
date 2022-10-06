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
          :class="[this.errors.length > 0 && this.isSubmitted ? 'is-invalid' : '']"
        >
      </div>

      <!-- Character limit warning (before submission) -->
      <p v-if="this.overLimit" class="p-2 text-start text-danger">
        {{this.warning}}
      </p>

      <!-- Show errors -->
      <div v-if="this.errors.length == 1 && this.isSubmitted" class="text-start text-danger">
        <!-- <p class="text-start text-danger">
          Please fix these errors:
        </p> -->
        <p class="ps-2 text-start text-danger">
          {{ this.errors[0] }}
        </p>
      </div>
      <div v-if="this.errors.length > 1 && this.isSubmitted" class="text-start text-danger">
        <!-- <p class="text-start text-danger">
          Please fix these errors:
        </p> -->
        <ul class="ps-4">
          <li v-for="(error, index) in this.errors" v-bind:key="index">
            {{ error }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
  
<script>
  export default {
    // props: {
    //   label: {
    //     type: String,
    //     default: ''
    //   },
    //   modelValue: {
    //     type: [String, Number],
    //     default: ''
    //   },
    //   limit: {
    //     type: String,
    //     default: ''
    //   }
    // },
    data() {
      return {
        warning: "",
        overLimit: true,
      }
    },
    props: ['label', 'modelValue', 'limit', 'errors', 'isSubmitted'],
    methods: {
      checkChar(){
        if (this.modelValue.length > Number(this.limit)) {
          var excess = this.modelValue.length - Number(this.limit)
          this.warning = "You are " + excess + " character(s) over the limit!"
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