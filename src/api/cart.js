import request from '@/utils/request'

var BASE_URL = '/api_v1/cart'
var ADMIN_BASE_URL = '/api_v1/cart/admin'


export function getCartByUser(id, name) {
  return request({
    url:  BASE_URL + '/one_cart?user_id='+id,
    method: 'get',
  })
}

export function addCart(data) {
  return request({
    url: BASE_URL + '/add_cart',
    method: 'post',
    data
  })
}

export function updateCart(data) {
  return request({
    url: BASE_URL + '/update_cart',
    method: 'put',
    data
  })
}

export function deleteCart(id) {
  return request({
    url: BASE_URL + '/del_cart?id='+id,
    method: 'delete',
  })
}


// ADMIN PART
export function getAllCarts() {
  return request({
      url: ADMIN_BASE_URL + '/all_carts',
      method: 'get',
  })
}