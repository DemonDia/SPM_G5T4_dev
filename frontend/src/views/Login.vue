<template>
  <div>
    <div class="sidenav">
      <div class="login-main-text">
        <h2>
          LJMS<br />
          Login Page
        </h2>
        <p>Login from here to access.</p>
      </div>
    </div>
    <div class="main">
      <div class="col-md-6 col-sm-12">
        <div class="login-form">
          <form prevent.default="">
            <div class="form-group">
              <label>User Name</label>
              <input v-model="username" type="text" class="form-control" placeholder="User Name" />
            </div>
            <div class="form-group">
              <label>Password</label>
              <input
                v-model="password"
                type="password"
                class="form-control"
                placeholder="Password"
              />
            </div>
            <button type="submit" class="btn btn-black mt-2">Login</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions({
      login: "auth/login",
    }),
    login() {
      this.login({
        username: this.username,
        password: this.password,
      });
    },
  },
};
</script>

<style scoped>

.sidenav {
  height: 100%;
  background-color: #000;
  overflow-x: hidden;
  padding-top: 20px;
}

.main {
  padding: 0px 20px;
}

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
}

@media screen and (max-width: 450px) {
  .login-form {
    margin-top: 10%;
  }

  .register-form {
    margin-top: 10%;
  }
}

@media screen and (min-width: 768px) {
  .main {
    margin-left: 40%;
  }

  .sidenav {
    width: 40%;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
  }

  .login-form {
    margin-top: 80%;
  }

  .register-form {
    margin-top: 20%;
  }
}

.login-main-text {
  margin-top: 20%;
  padding: 60px;
  color: #fff;
}

.login-main-text h2 {
  font-weight: 300;
}

.btn-black {
  background-color: #000 !important;
  color: #fff;
}
</style>
