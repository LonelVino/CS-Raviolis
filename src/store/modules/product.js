const state = {
  products: [],
  productByCat: [],
  categories: [],
  prods_loading: false,
}

const mutations = {
  SET_PRODUCTS: (state, prods) => {
    state.products = prods
  },
  ADD_PRODUCT: (state, product) => {
    state.products.push(product)
  },
  CLEAR_PRODUCTS: (state) => {
    state.products.splice(0)
  },
  SET_PRODUCTS_BYCAT: (state, prods) => {
    state.productByCat = prods
  },
  ADD_PRODUCT_BYCAT: (state, product) => {
    state.productByCat.push(product)
  },
  CLEAR_PRODUCTS_BYCAT: (state) => {
    state.productByCat.splice(0)
  },
  SET_CATEGORIES: (state, cats) => {
    state.categories = cats
  },
  ADD_CATEGORY: (state, cat) => {
    state.categories.push(cat)
  },
  CLEAR_CATEGORIES: (state) => {
    state.categories.splice(0)
  },
  CHANGE_PRODS_LOADING: (state, status) => {
    state.prods_loading = status
  }
}

const actions = {
  setProducts({ commit }, prods) {
    commit('SET_PRODUCTS', prods)
  },
  addProduct({ commit }, product) {
      commit('ADD_PRODUCT', product)
  },
  clearProducts({ commit }) {
      commit('CLEAR_PRODUCTS')
  },
  setProductsByCat({ commit }, prods) {
    commit('SET_PRODUCTS_BYCAT', prods)
  },
  addProductByCat({ commit }, product) {
      commit('ADD_PRODUCT_BYCAT', product)
  },
  clearProductsByCat({ commit }) {
      commit('CLEAR_PRODUCTS_BYCAT')
  },
  setCategories({ commit }, cats) {
    commit('SET_CATEGORIES', cats)
  },
  addProduct({ commit }, cat) {
      commit('ADD_CATEGORY', cat)
  },
  clearCategories({ commit }) {
      commit('CLEAR_CATEGORIES')
  },
  changeProdsLoading({ commit }, status) {
      commit('CHANGE_PRODS_LOADING', status)
  }
}

export default {
namespaced: true,
state,
mutations,
actions
}
  