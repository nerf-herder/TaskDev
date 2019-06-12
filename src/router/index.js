import Vue from 'vue';
import Vuetify from 'vuetify';
import VeeValidate from 'vee-validate';
import 'vuetify/dist/vuetify.min.css';
import Router from 'vue-router';
import Datetime from 'vue-datetime'
// You need a specific loader for CSS files
import 'vue-datetime/dist/vue-datetime.css'

Vue.use(Datetime)

Vue.use(Router);
Vue.use(Vuetify);
Vue.use(VeeValidate);

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Navigation',
      component: () => import('@/views/Tasks'),
    },
    {
      path: '/tasks',
      name: 'Tasks',
      component: () => import('@/views/Tasks'),
    },
  ],
});

export default router;
