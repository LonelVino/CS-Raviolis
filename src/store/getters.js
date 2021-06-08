const getters = {
  sidebar: state => state.app.sidebar,
  size: state => state.app.size,
  device: state => state.app.device,

  visitedViews: state => state.tagsView.visitedViews,
  cachedViews: state => state.tagsView.cachedViews,

  cas_id: state => state.user.cas_id,
  name: state => state.user.name,
  user_id: state => state.user.user_id,
  role: state => state.user.role,
  
  products: state => state.product.products,
  productByCat: state => state.product.productByCat,
  categories: state => state.product.categories,
  prods_loading: state => state.product.prods_loading,

  permission_routes: state => state.permission.routes,
  errorLogs: state => state.errorLog.logs
}
export default getters
