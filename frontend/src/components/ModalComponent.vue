<template>
    <div class="modal fade" id="submitModal" tabindex="-1" aria-labelledby="submitModalLabel" aria-hidden="true">
        <span>{{ checkSuccess() }}</span>
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="submitModalLabel">
                    {{this.header}}
                </h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div>
                    <i :class="icon" style="font-size: 5rem" :style="{ 'color': isSuccess ? '#87C60A' : '#F19104'}"></i>
                </div>
                <div>
                    {{this.message}}
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
            </div>
        </div>
    </div>
</template>
  
<script>
    export default {
    name: "ModalComponent",
    props: ["type", "errors"],
    data() {
        return {
            isSuccess: false,
            header: "",
            icon: "",
            message: ""
        }
    },
    methods: {
        checkSuccess() {
            if (this.errors.length == 0) {
                this.isSuccess = true
                this.header = "Success!"
                this.icon = "bi bi-emoji-smile-fill icon-green"
                this.message = this.type + " created successfully."
            }
            else {
                this.isSuccess = false
                this.header = "Try again!"
                this.icon = "bi bi-emoji-frown-fill icon-red"
                this.message = this.type + " is unsuccessfully created. Please fix the errors."
            }
        }
    }
    };

</script>
  
<style scoped>
  i {
    width: 30px;
  }
</style>  