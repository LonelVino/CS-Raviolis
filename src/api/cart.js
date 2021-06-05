import request from '@/utils/request'

var BASE_URL = '/api_v1/cart'
var ADMIN_BASE_URL = '/api_v1/cart/admin'


export function getCartByUser(id) {
  return request({
    url:  BASE_URL + '/one_cart?usr_id='+id,
    method: 'get',
  })
}


export function getCartItems(id) {
  return request({
    url:  BASE_URL + '/cart_items?cart_id='+id,
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

export function updateCartItem(data) {
  return request({
    url: BASE_URL + '/update_cart_item',
    method: 'put',
    data
  })
}

export function deleteCart(id) {
  return request({
    url: BASE_URL + '/delete_cart?id='+id,
    method: 'delete',
  })
}



export function deleteCartItem(id) {
  return request({
    url: BASE_URL + '/delete_crt_item?id='+id,
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