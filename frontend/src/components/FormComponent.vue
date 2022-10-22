<template>
  <div class="row d-flex justify-content-center my-sm-2 my-md-5 ms-0 pe-3">
    <div class="col-sm-12 col-md-3 text-xs-start text-sm-center pt-1 px-0">
        <label class="form-label pt-1" v-if="label">
          {{ label }}
        </label>
    </div>
    <div class="col-sm-12 col-md-9 px-0">
      <div>
        <!-- If input text box -->
        <input v-if="this.formType=='input'"
          v-bind="$attrs"
          :value="modelValue"
          :placeholder="label"
          @input="$emit('update:modelValue', $event.target.value)"
          v-on:keyup="this.checkChar"
          class="form-control"
          :class="[this.errors.length > 0 ? 'is-invalid' : '']"
        >
        <textarea v-else-if="this.formType=='textarea'"
          v-bind="$attrs"
          :value="modelValue"
          :placeholder="label"
          @input="$emit('update:modelValue', $event.target.value)"
          v-on:keyup="this.checkChar"
          class="form-control"
          :class="[this.errors.length > 0 ? 'is-invalid' : '']"
        ></textarea>
      </div>
      <div class="row">
        <div class="text-start text-danger col-sm-12" :class="this.formType=='textarea' ? 'col-lg-8' : 'col-lg-10'">
          <!-- Character limit warning (before submission) -->
          <p v-if="this.overLimit" class="pt-2">
            {{ this.warning }}
          </p>
          <!-- Show errors -->
          <div v-if="this.errors.length == 1">
            <p>
              {{ this.errors[0] }}
            </p>
          </div>
          <div v-if="this.errors.length > 1">
            <ul>
              <li v-for="(error, key) in this.errors" :key="key">
                {{ error }}
              </li>
            </ul>
          </div>
        </div>
        <!-- Word count for text area -->
        <div class="col-sm-12 col-lg-4">
          <p class="text-sm-start text-lg-end pt-2" v-if="this.formType=='textarea'" :class="this.overLimit ? 'text-danger' : ''">
            Word count: <strong>{{modelValue.length}}</strong>/{{this.limit}}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
  export default {
    name: "FormComponent",
    data() {
      return {
        warning: "",
        overLimit: false,
      }
    },
    props: ['label', 'modelValue', 'limit', 'errors', 'isSubmitted', 'formType'],
    methods: {
      checkChar(){
        if (this.modelValue.length > Number(this.limit)) {
          var excess = this.modelValue.length - Number(this.limit)
          this.warning = "WARNING: You are " + excess + " character(s) over the limit!"
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
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
  }
</style>