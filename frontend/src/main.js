import './plugins/axios'
import { createApp } from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

createApp(App).use(store).use(Vuex).use(router).mount('#app')
