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
          <div class="alert alert-danger" role="alert" v-if="error.length > 0">
            {{ this.error }}
          </div>
          <form @submit.prevent="signin" method="POST">
        

            <select name="cars" id="cars" v-model="userType" @change="changeRole">
            <option v-for="(value, key) in roles" v-bind:key="key">{{key}}</option>
            </select>

            <div class="form-group">
              <label>Staff ID</label>
              <input
                v-model="form.staffID"
                type="text"
                class="form-control"
                name="staffID"
                placeholder="Email/Staff ID"
              />
            </div>
            <div class="form-group">
              <label>Password</label>
              <input
                v-model="form.password"
                type="password"
                name="password"
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
      form: {
        staffID: "130001",
        password: "123456",
      },
      roles: {
        Admin: {
          staffID: "130001",
          password: "123456",
        },
        User: {
          staffID: "140003",
          password: "123456",
        },
        Manager: {
          staffID: "140001",
          password: "123456",
        },
        Trainer: {
          staffID: "150175",
          password: "123456",
        },
      },
      error: "",
      userType: "Admin",
    };
  },
  methods: {
    ...mapActions({
      login: "auth/login",
    }),
    signin() {
      this.login({
        staffID: this.form.staffID,
        password: this.form.password,
      })
        .then(() => {
          this.$router.replace({ name: "learningjourney" }).catch(() => {
          });
        })
        .catch(() => {
          this.error = "Invalid email or password";
        });
    },
    changeRole() {
      this.form.staffID = this.roles[this.userType].staffID;
      this.form.password = this.roles[this.userType].password;
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
  background: #fff;
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
