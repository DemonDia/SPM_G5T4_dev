<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-white">
    
      <div class="container-fluid">
        <div class="header-logo">
          <router-link to="/" class="navbar-brand">{{ title }}</router-link>
        </div>
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
          <span id="toggle-title">Menu</span>
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
        <div class="header-navigation-actions">
          <a href="#" class="icon-button">
            <i class="ph-gear-bold"></i>
          </a>
          <a @click="signOut" class="icon-button">
            <i class="ph-sign-out-bold"></i>
          </a>
          <a href="#" class="avatar">
            <img v-bind:src="imageURL" alt="" />
          </a>
        </div>
        </div>
      
    </nav>

    <!-- Main Content -->

    <slot />
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";

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
  data() {
    return {};
  },
  methods: {
    ...mapActions({
      logout: "auth/signout",
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
    imageURL() {
      if (this.user) {
        return "https://ui-avatars.com/api/?name=" + this.user.Staff_FName + "+" + this.user.Staff_LName;
      } else {
        return "https://ui-avatars.com/api/?background=random";
      }

    },
    },
};
</script>
<style scoped>

.header-content {
    display: flex;
    align-items: center;
}

.responsive-wrapper {
    width: 90%;
    max-width: 1280px;
    margin-left: auto;
    margin-right: auto;
}
.header-logo {
  margin-left: 2.5em;
}
.navbar {
  border-bottom: 1px solid var(#eff1f6);
  background-color: var(#fff);
}

.navbar-collapse {
  flex-grow: 0;
  align-items: start !important;
}

.collapse.navbar-collapse a {
  text-decoration: none;
  color: #404089;
  font-weight: 800;
  transition: 0.15s ease;
  margin-left: 1.5rem;
}

.collapse.navbar-collapse a:hover,
.collapse.navbar-collapse a:focus {
    color: #434ce8;
    border-bottom: 3px solid #434ce8;
    text-decoration: none;
}

.navbar-toggler {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.875rem !important;
  transition: 0.15s ease !important;
}
.navbar-toggler:hover {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  color: #404089;
  font-size: 0.875rem !important;
  transition: 0.15s ease !important;
}

.navbar-toggler:hover .navbar-toggler-icon {
  font-size: 0.875rem !important;
}

#toggle-title {
  margin-left: 0.5rem;
}

.header-navigation {
    display: flex;
    flex-grow: 1;
    align-items: center;
    justify-content: space-between;
}

.header-navigation-actions {
  display: flex;
  align-items: center;
}
.header-navigation-actions > .avatar {
  margin-left: 0.75rem;
}
.header-navigation-actions > .icon-button + .icon-button {
  margin-left: 0.25rem;
}
.header-navigation-actions > .button + .icon-button {
  margin-left: 1rem;
}

.icon-button {
  font: inherit;
  color: inherit;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  color: #404089;
  transition: 0.15s ease;
}
.icon-button i {
  font-size: 1.25em;
}
.icon-button:focus,
.icon-button:hover {
  background-color: #ecf3fe;
  color: #434ce8;
}

.avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 1200px) {
  .header-navigation-actions {
    display: none;
  }
}

</style>
