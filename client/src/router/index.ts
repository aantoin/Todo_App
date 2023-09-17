import { createRouter, createWebHistory } from 'vue-router'
import HomeLayout from '@/layouts/HomeLayout.vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import { useAuthStore } from '@/stores/auth'
import { useChecklistStore } from '@/stores/checklists'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),
      meta: { layout: HomeLayout }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue'),
      meta: { layout: HomeLayout }
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/SignupView.vue'),
      meta: { layout: HomeLayout }
    },
    {
      path: '/signout',
      name: 'signout',
      component: () => import('@/views/HomeView.vue'),
      meta: { layout: HomeLayout },
      beforeEnter: (to,from,next) => {
        const authStore = useAuthStore();
        const checklistStore = useChecklistStore();
        checklistStore.resetLocalData();
        authStore.logout();
        next({ name: 'login' });
      }
    },
    {
      path: '/u',
      name: 'dashboard',
      component: () => import('@/views/DashboardView.vue'),
      meta: { layout: DashboardLayout }
    },
    {
      path: '/u/new',
      name: 'new_checklist',
      component: () => import('@/views/NewChecklistView.vue'),
      meta: { layout: DashboardLayout }
    },
    {
      path: '/u/:id',
      name: 'checklist_detail',
      component: () => import('@/views/ChecklistDetailView.vue'),
      meta: { layout: DashboardLayout }
    },
    {
      path: '/auth/confirm-email/:key',
      name: 'confirm-email',
      component: () => import('../views/auth/ConfirmEmailView.vue')
    }
  ]
})

export default router
