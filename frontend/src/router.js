import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/profile',
      component: () => import('./views/Profile.vue')
    },
    {
      path: '/settings',
      component: () => import('./views/Settings.vue')
    },
    {
      path: '/messages',
      component: () => import('./views/Messages.vue')
    }
  ]
});
