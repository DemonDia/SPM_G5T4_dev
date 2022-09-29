<template>
    <a class="nav-link" v-bind="$attrs">
        <slot>
            <p>{{link.name}}</p>
      </slot>
    </a>
</template>
<script>
    export default {
      inheritAttrs: false,
      props: {
        link: {
          type: [String, Object],
          default: () => {
            return {
              name: '',
              path: ''
            }
          }
        },
        tag: {
          type: String,
          default: 'router-link'
        }
      },
      methods: {
        
      }
    }
  </script>
  <style>
  </style>