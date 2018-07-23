import Vue from 'vue'
import Router from 'vue-router'
import About from './views/About.vue'
import Maincomp from './views/Maincomp.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'mainVue',
      component: Maincomp
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }
  ]
})
