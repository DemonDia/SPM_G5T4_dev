<template>
    <div class="modal fade" id="submitModal" tabindex="-1" aria-labelledby="submitModalLabel" aria-hidden="true">
        <span>{{ checkSuccess() }}</span>
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="submitModalLabel">
                    {{this.header}}
                </h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="onClickButton()"></button>
            </div>
            <div class="modal-body text-center">
                <div>
                    <i :class="icon" style="font-size: 5rem" :style="{ 'color': isSuccess ? '#87C60A' : '#F19104'}"></i>
                </div>
                <div class="msg">
                    {{this.message}}
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="onClickButton">Close</button>
            </div>
            </div>
        </div>
    </div>
</template>
  
<script>
    export default {
    name: "ModalComponent",
    props: ["type", "isSuccess", "func"],
    data() {
        return {
            header: "",
            icon: "",
            message: "",
        }
    },
    methods: {
        checkSuccess() {
            var splitStr = this.type
            splitStr = splitStr.toLowerCase().split(' ');
            for (var i = 0; i < splitStr.length; i++) {
                splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);     
            }
            var newType = splitStr.join(' '); 
            if (this.isSuccess) {
                this.header = "Success!"
                this.icon = "bi bi-emoji-smile-fill icon-green"
                this.message = "Yay! " + newType + " is " + this.func + "d successfully."
            }
            else {
                this.header = "Try again!"
                this.icon = "bi bi-emoji-frown-fill icon-red"
                this.message = "Oops, " + newType + " is unsuccessfully " + this.func + "d. Please fix the errors and try again!"
            }
        },
        onClickButton(event) {
            console.log("clicked modal close button");
            this.$emit('clicked', false);
        }
    },
};

</script>
  
<style scoped>
    i {
        width: 30px;
    }

    .msg:first-letter{
        text-transform: capitalize
    }
</style>  