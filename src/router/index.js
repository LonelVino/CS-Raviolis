import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'
import tableRouter from './modules/table'


/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */

export const constantRoutes = [
  // {
  //   path: '/',
  //   component: () => import('@/views/login/index'),
  //   redirect: '/login',
  //   name: 'MainPage',
  // },
  {
    path: '/404',
    component: () => import('@/views/error-page/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/error-page/401'),
    hidden: true
  },
  { 
    path: '/login', 
    name: 'Login',
    component: () => import('@/views/login/index'),
  },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/login',
  //   children: [
  //     {
  //       path: 'login',
  //       component: () => import('@/views/login/index'),
  //       name: 'Dashboard',
  //       meta: { title: 'Login', icon: 'login', affix: true }
  //     }
  //   ]
  // },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/dashboard/index'),
        name: 'Dashboard',
        meta: { title: 'Dashboard', icon: 'dashboard', affix: true }
      }
    ]
  },
  {
    path: '/profile',
    component: Layout,
    redirect: '/profile/index',
    hidden: true,
    children: [
      {
        path: 'index',
        component: () => import('@/views/profile/index'),
        name: 'Profile',
        meta: { title: 'Profile', icon: 'user', noCache: true }
      }
    ]
  },
  {
    path: '/cart-table',
    component: Layout,
    children: [
      {
        path: '/cart-table',
        component: () => import('@/views/cart-table/index'),
        name: 'CartTable',
        meta: { title: 'CartTable', icon: 'dashboard', affix: true }
      }
    ]
  },

  {
    path: '/user-table',
    component: Layout,
    children: [
      {
        path: '/user-table',
        component: () => import('@/views/user-table/index'),
        name: 'UserTable',
        meta: { title: 'UserTable', icon: 'dashboard', affix: true }
      }
    ]
  },
  {
    path: '/table',
    component: Layout,
    redirect: '/table/ane-table',
    name: 'Table',
    children: [
      {
        path: 'ane-table',
        component: () => import('@/views/table/aneTable'),
        name: 'AneTable',
        meta: { title: 'Ane Rouge' }
      },
    ]
  }
]

export const asyncRoutes = [
  tableRouter,
]


const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()


export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}


export default router