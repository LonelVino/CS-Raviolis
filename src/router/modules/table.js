
import Layout from '@/layout'
const tableRouter = {
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
export default tableRouter
