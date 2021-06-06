
import Layout from '@/layout'
const tableRouter = {
    path: '/table',
    component: Layout,
    redirect: '/table/check-table',
    name: 'AdminTable',
    children: [
        {
          path: 'order-table',
          component: () => import('@/views/table/orderTable'),
          name: 'OrderTable',
          meta: { title: 'Order Table' }
        },
        {
          path: 'order-item-table',
          component: () => import('@/views/table/orderItemTable'),
          name: 'OrderItemTable',
          meta: { title: 'Order-Item Table' }
        },
        {
          path: 'cart-table',
          component: () => import('@/views/table/cartTable'),
          name: 'CartTable',
          meta: { title: 'Cart Table' }
        },
        {
          path: 'check-table',
          component: () => import('@/views/table/checkTable'),
          name: 'CheckTable',
          meta: { title: 'Check Table' }
        },
        {
          path: 'product-table',
          component: () => import('@/views/table/productTable'),
          name: 'ProductTable',
          meta: { title: 'Product Table' }
        },
        {
          path: 'category-table',
          component: () => import('@/views/table/categoryTable'),
          name: 'CategoryTable',
          meta: { title: 'Category Table' }
        },
      ]
    }
export default tableRouter
