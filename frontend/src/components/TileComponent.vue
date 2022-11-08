<template>
    <div class="radio-tile-group" @click="onClickButton">
      <div class="input-container">
          <input :type="this.type" name="radio" :checked="isSelected()">
          <div class="radio-tile text-center p-1 text-break">
            <label>{{name}}</label>
          </div>
      </div>
    </div>
</template>
  
<script>
  export default {
    name: "TileComponent",
    data() {
      return {
        checked: false
      }
    },
    props: ["name", "id", "type", "selected", "itemType"],
    methods: {
      onClickButton(event) {
        this.$emit('clicked', {id: this.id, name: this.name, type: this.type, itemType: this.itemType});
      },

      isSelected() {
        if (this.type == "radio") {
          if (this.selected == this.id) {
            return true;
          } else {
            return false;
          }
        } else {
          if (this.selected.includes(this.id)) {
            return true;
          } else {
            return false;
          }
        }
      }
    },
  };
</script>
  
<style scoped>
  .radio-tile-group {
    flex-wrap: wrap;
    justify-content: center;
  }

  .input-container {
    position: relative;
    height: 8rem;
    margin: 0.5rem;
  }

  .input-container input {
    position: absolute;
    height: 100%;
    width: 100%;
    margin: 0;
    cursor: pointer;
    z-index: 2;
    opacity: 0;
  }

  .input-container .radio-tile {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    border: 2px solid #404089;
    border-radius: 8px;
    transition: all 300ms ease;
  }

  .input-container label {
    color: #404089;
    font-size: 0.80rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  input:checked+.radio-tile {
    background-color: #404089;
    box-shadow: 0 0 6px #9797c9;
    transform: scale(1.1);
  }

  input:hover+.radio-tile {
    box-shadow: 0 0 12px #404089;
  }

  input:checked+.radio-tile label {
    color: white;
  }

  @media screen and (max-width: 575px) {
    .input-container {
      min-width: 10rem;
    }
  }

  @media screen and (min-width: 576px) {
    .input-container {
      width: 10rem;
    }
  }
</style>
  