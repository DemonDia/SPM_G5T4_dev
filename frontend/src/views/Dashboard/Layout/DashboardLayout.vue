<template>
  <div>
    <!-- Menu for HR -->
    <nav class="navbar navbar-expand-lg bg-white">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">{{ title }}</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarText"
        aria-controls="navbarText"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mx-auto mb-2 mb-lg-0" v-for="(link, index) in topMenuLinks" :key="link.name + index" :to="link.path" :link="link">
              <li class="nav-item">
                <router-link class="nav-link" :to="link.path">{{link.name}}</router-link>
              </li>
        </ul>
      </div>
    </div>
  </nav>

    <!-- Main Content -->

    <slot />
  </div>
</template>
<script>
export default {
  components: {
    
  },
  props: {
    title: {
      type: String,
      default: "LJMS",
    },
    topMenuLinks: {
      type: Array,
      default: () => [
          {name: 'Home',path: '/'},
          {name: 'Roles',path: '/roles'},
          {name: 'Skills',path: '/skills'},
          {name: 'Courses',path: '/courses'},
          {name: 'Learning Journey',path: '/learningjourney'},
      ],
    },
  },
  data() {},
  methods: {},
};
</script>
<style scoped>

</style>