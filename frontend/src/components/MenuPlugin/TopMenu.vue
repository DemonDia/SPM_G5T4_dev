<template>
    <div class="topmenu">
      <div class="topmenu-wrapper">
        <div class="logo">
          <a href="#" class="simple-text">
            {{title}}
          </a>
        </div>
  
        <slot name="content"></slot>
        <ul>
          <!--By default vue-router adds an active class to each route link. This way the links are colored when clicked-->
          <slot>
            <topmenu-link v-for="(link,index) in topMenuLinks"
                          :key="link.name + index"
                          :to="link.path"
                          :link="link">
              <p>{{link.name}}</p>
            </topmenu-link>
          </slot>
        </ul>
      </div>
    </div>
  </template>
  <script>
    import TopMenuLink from './TopMenuLink.vue'
  
    export default {
      components: {
        TopMenuLink
      },
      props: {
        title: {
          type: String,
          default: 'Learning Journey Management System'
        },
        topMenuLinks: {
          type: Array,
          default: () => []
        },
      },
    }
  
  </script>
  <style>
   
  </style>