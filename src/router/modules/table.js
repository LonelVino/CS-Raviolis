
import Layout from '@/layout'
const tableRouter = {
    path: '/table',
    component: Layout,
    redirect: '/table/pitch-table',
    name: 'Table',
    children: [
        {
          path: 'pitch-table',
          component: () => import('@/views/table/pitchTable'),
          name: 'PitchTable',
          meta: { title: 'Pitch' }
        },
        {
          path: 'ane-table',
          component: () => import('@/views/table/aneTable'),
          name: 'AneTable',
          meta: { title: 'Ane Rouge' }
        },
        {
          path: 'vol-table',
          component: () => import('@/views/table/volTable'),
          name: 'VolantTable',
          meta: { title: 'Volant Volant' }
        }
      ]
    }
export default tableRouter
