import './plugins/axios'
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import Vuex from 'vuex'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"


require('./store/subscriber')

store.dispatch('auth/attempt', localStorage.getItem('token'))

createApp(App).use(store).use(Vuex).use(router).use(axios).mount('#app')
