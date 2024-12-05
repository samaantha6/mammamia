import { createRouter, createWebHistory } from 'vue-router';
import AgendaContactos from '@/components/AgendaContactos.vue';

const routes = [
  {
    path: '/contactos',
    name: 'AgendaContactos',
    component: AgendaContactos,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;