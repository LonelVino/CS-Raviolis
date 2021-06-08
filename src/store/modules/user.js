import { register, login, logout, getRole, getName, getInfo, getAllInfos } from '@/api/user'
import router, { resetRouter } from '@/router'

const state = {
  cas_id: 0,
  name: '',
  user_id: 1,
  role: 'admin',
}

const mutations = {
  SET_CAS_ID: (state, cas_id) => {
    state.cas_id = cas_id
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_USER_ID: (state, user_id) => {
    state.user_id = user_id
  },
  SET_ROLE: (state, role) => {
    state.role = role
  },
}

const actions = {
  setUserId({ commit }, user_id) {
    commit('SET_USER_ID', user_id)
  },

  register({ commit }, userInfo) {
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      register({ username: username.trim(), password: password }).then(response => {
        resolve()
        return response;
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user login
  login({ commit, state }, userInfo) {
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password }).then(response => {
        const { data } = response
        commit('SET_CAS_ID', data.id)
        commit('SET_ROLE', data.role)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },
  getRole({commit}, cas_id) {
    return new Promise((resolve, reject) => {
      getRole(cas_id).then(response => {
        const { data } = response
        console.log(data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  // get one user name
  getName({ commit, state }, id) {
    return new Promise((resolve, reject) => {
      getName(id).then(response => {
        const { data } = response
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get one user info
  getInfo({ commit, state }, id=2, name='') {
    return new Promise((resolve, reject) => {
      getInfo(id, name).then(response => {
        const { data } = response
        console.log('Information: ', data)
        if (!data) {
          reject('Verification failed, please Login again.')
        }

        // commit('SET_ROLES', roles)
        // commit('SET_NAME', name)
        resolve(data)
        return data
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get all users' infos
  getAllInfos() {
    return new Promise((resolve, reject) => {
      getAllInfos().then(response => {
        const {data} = response
        console.log('all infos:', data)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get all users' names
  getAllNames() {
    return new Promise((resolve, reject) => {
      getAllNames().then(response => {
        const {data} = response
        console.log('All Names are:', data)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state, dispatch }) {
    return new Promise((resolve, reject) => {
      logout().then(() => {
        commit('SET_ROLES', 'editor')
        commit('SET_CAS_ID', 0)
        resetRouter()

        // reset visited views and cached views
        // to fixed https://github.com/PanJiaChen/vue-element-admin/issues/2485
        // dispatch('tagsView/delAllViews', null, { root: true })

        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // dynamically modify permissions
  async changeRoles({ commit, dispatch }, role) {

    const { roles } = await dispatch('getInfo')

    resetRouter()

    // generate accessible routes map based on roles
    const accessRoutes = await dispatch('permission/generateRoutes', roles, { root: true })
    // dynamically add accessible routes
    router.addRoutes(accessRoutes)

    // reset visited views and cached views
    dispatch('tagsView/delAllViews', null, { root: true })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
