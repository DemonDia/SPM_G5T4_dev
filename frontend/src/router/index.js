import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RoleView from '../views/RoleView.vue'
import CourseView from '../views/CourseView.vue'
import SkillView from '../views/SkillView.vue'
import LJView from '../views/LJView.vue'
import CreateRole from '../views/CreateRole.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/create-role',
    name: 'create-role',
    component: CreateRole
  },
  {
    path: '/roles',
    name: 'roles',
    component: RoleView
  },
  {
    path: '/courses',
    name: 'courses',
    component: CourseView
  },
  {
    path: '/skills',
    name: 'skills',
    component: SkillView
  },
  {
    path: '/learningjourney',
    name: 'learningjourney',
    component: LJView
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
