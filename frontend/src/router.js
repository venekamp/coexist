import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

import store from './store';

Vue.use(Router);

const routes = [
  { path: '/', component: Home },
  {
    path: '/login',
    component: () => import('./views/Login.vue'),
    noauth: true
  },
  { path: '/profile', component: () => import('./views/Profile.vue') },
  { path: '/settings', component: () => import('./views/Settings.vue') },
  { path: '/messages', component: () => import('./views/Messages.vue') },
  { path: '/help', component: () => import('./views/Help.vue'), noauth: true }
];

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: routes
});

router.beforeEach((to, from, next) => {
  if (!store.state.hasAuthenticatedUser) {
    const route = routes.find(route => route.path === to.path);
    if (route.noauth) {
      next();
    } else {
      next({ path: 'login' });
    }
  } else {
    next();
  }
});

export default router;
