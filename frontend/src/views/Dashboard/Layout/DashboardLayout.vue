<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-white">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">{{ title }}</router-link>
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
          <template v-if="authenticated && user.Role == 1">
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

          <!-- Staff Menu Links-->
          <template v-if="authenticated && user.Role == 2">
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

          <!-- Manager Menu Links-->
          <template v-if="authenticated && (user.Role == 3 || user.Role == 4)">
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

          
        </div>
      </div>
    </nav>

    <!-- Main Content -->

    <slot />
  </div>
</template>
<script>
import { mapGetters,mapActions } from "vuex";

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
  },
  data() {},
  methods: {
    ...mapActions({
      logout: "auth/logout",
    }),
    signOut() {
      this.logout().then(() => {
        this.$router.replace({ name: "login" });
      });
    },

  },
  computed: {
    ...mapGetters({
      user: "auth/user",
      authenticated: "auth/authenticated",
    }),
  },
};
</script>
<style scoped></style>
