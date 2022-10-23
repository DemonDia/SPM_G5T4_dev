import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RoleView from '../views/RoleView.vue'
import CourseView from '../views/CourseView.vue'
import SkillView from '../views/SkillView.vue'
import LJView from '../views/LJView.vue'
import CreateRole from '../views/CreateRole.vue'
import CreateSkill from '../views/CreateSkill.vue'
import Login from '../views/Login.vue'
import store from '@/store'
import UpdateRole from '../views/UpdateRole.vue'
import UpdateCourse from '../views/UpdateCourse.vue'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/',
    name: 'home',
    component: HomeView,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        
        return next({ name: 'login' })
      }
      next()
    },
  },
  {
    path: '/create-role',
    name: 'create-role',
    component: CreateRole,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }

      if (store.getters['auth/user'].Role != 1) {
        return next({ name: 'home' })
      }

      next()
    },
  },
  {
    path: '/update-role/:role_id',
    name: 'update-role',
    component: UpdateRole,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }

      if (store.getters['auth/user'].Role != 1) {
        return next({ name: 'home' })
      }

      next()
    },
  },
  {
    path: '/update-course/:course_id',
    name: 'update-course',
    component: UpdateCourse,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }

      if (store.getters['auth/user'].Role != 1) {
        return next({ name: 'home' })
      }

      next()
    },
  },
  {
    path: '/create-skill',
    name: 'create-skill',
    component: CreateSkill,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }

      if (store.getters['auth/user'].Role != 1) {
        return next({ name: 'home' })
      }
      
      next()
    },
  },
  {
    path: '/roles',
    name: 'roles',
    component: RoleView,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }
      next()
    },
  },
  {
    path: '/courses',
    name: 'courses',
    component: CourseView,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }
      next()
    },
  },
  {
    path: '/skills',
    name: 'skills',
    component: SkillView,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }
      
      if (store.getters['auth/user'].Role != 1) {
        return next({ name: 'home' })
      }
      
      next()
    },
  },
  {
    path: '/learningjourney',
    name: 'learningjourney',
    component: LJView,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        return next({ name: 'login' })
      }
      next()
    },
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
