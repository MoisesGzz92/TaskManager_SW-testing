import { createRouter, createWebHistory } from 'vue-router'
import TaskList from '../views/TaskListPage.vue'
import TaskForm from '../views/TaskFormPage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'TaskList',
      component: TaskList,
    },
    {
      path: '/task/create',
      name: 'TaskCreate',
      component: TaskForm,
    }
  ]
})

export default router
