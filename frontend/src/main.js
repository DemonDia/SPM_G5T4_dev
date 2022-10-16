import './plugins/axios'
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import Vuex from 'vuex'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import moshaToast from 'mosha-vue-toastify'
import 'mosha-vue-toastify/dist/style.css'


require('./store/subscriber')

store.dispatch('auth/attempt', localStorage.getItem('token')).then(() => {
    createApp(App).use(store).use(Vuex).use(router).use(axios).use(moshaToast).mount('#app')
})


