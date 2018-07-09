import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Fauna from './views/Fauna.vue'
import FaunaForm from './components/FaunaForm.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/fauna',
      name: 'fauna',
      component: Fauna
    },
    {
	  path: '/edit/fauna/:id',
	  name: 'fauna_edit',
	  component: FaunaForm
	}
  ]
})
