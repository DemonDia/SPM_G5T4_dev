<template>
  <div>
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
          <!-- HR Menu Links-->
          <template v-if="authenticated && user.role == 'Admin'">
            <ul
              class="navbar-nav mx-auto mb-2 mb-lg-0"
              v-for="(link, index) in HRMenuLinks"
              :key="link.name + index"
              :to="link.path"
              :link="link"
            >
              <li class="nav-item">
                <router-link class="nav-link" :to="link.path">{{
                  link.name
                }}</router-link>
              </li>
            </ul>
          </template>

          <!-- Manager Menu Links-->
          <template v-if="authenticated && user.role == 'Manager'">
            <ul
              class="navbar-nav mx-auto mb-2 mb-lg-0"
              v-for="(link, index) in ManagerMenuLinks"
              :key="link.name + index"
              :to="link.path"
              :link="link"
            >
              <li class="nav-item">
                <router-link class="nav-link" :to="link.path">{{
                  link.name
                }}</router-link>
              </li>
            </ul>
          </template>

          <!-- Staff Menu Links-->
          <template v-if="authenticated && user.role == 'Staff'">
            <ul
              class="navbar-nav mx-auto mb-2 mb-lg-0"
              v-for="(link, index) in StaffMenuLinks"
              :key="link.name + index"
              :to="link.path"
              :link="link"
            >
              <li class="nav-item">
                <router-link class="nav-link" :to="link.path">{{
                  link.name
                }}</router-link>
              </li>
            </ul>
          </template>

          <!-- Default Menu Links-->
          <template>
            <ul
              class="navbar-nav mx-auto mb-2 mb-lg-0"
              v-for="(link, index) in DefaultMenuLinks"
              :key="link.name + index"
              :to="link.path"
              :link="link"
            >
              <li class="nav-item">
                <router-link class="nav-link" :to="link.path">{{
                  link.name
                }}</router-link>
              </li>
            </ul>
          </template>
        </div>
      </div>
    </nav>

    <!-- Main Content -->

    <slot />
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  components: {},
  props: {
    title: {
      type: String,
      default: "LJMS",
    },
    HRMenuLinks: {
      type: Array,
      default: () => [
        { name: "Home", path: "/" },
        { name: "Roles", path: "/roles" },
        { name: "Skills", path: "/skills" },
        { name: "Courses", path: "/courses" },
        { name: "Learning Journey", path: "/learningjourney" },
      ],
    },
    ManagerMenuLinks: {
      type: Array,
      default: () => [
        { name: "Home", path: "/" },
        { name: "Roles", path: "/roles" },
        { name: "Skills", path: "/skills" },
        { name: "Courses", path: "/courses" },
        { name: "Learning Journey", path: "/learningjourney" },
      ],
    },
    StaffMenuLinks: {
      type: Array,
      default: () => [
        { name: "Home", path: "/" },
        { name: "Roles", path: "/roles" },
        { name: "Courses", path: "/courses" },
        { name: "Learning Journey", path: "/learningjourney" },
      ],
    },
    DefaultMenuLinks: {
      type: Array,
      default: () => [{ name: "Login", path: "/login" }],
    },
  },
  data() {},
  methods: {},
  computed: {
    ...mapGetters({
      user: "auth/user",
      authenticated: "auth/authenticated",
    }),
  },
};
</script>
<style scoped></style>
