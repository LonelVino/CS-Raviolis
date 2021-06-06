import request from '@/utils/request'

var BASE_URL = '/api_v1/order'
var ADMIN_BASE_URL = '/api_v1/order/admin'

// --------------------------------- User Part -----------------------
export function getOneOrderItem(id) {
  return request({
    url:  BASE_URL + '/one_ord_itm?id='+id,  //id: OrderItem.id
    method: 'get',
  })
}

// Get the realted order items according to the order_id
export function getOneOrderItems(ord_id) {
  return request({
    url:  BASE_URL + '/usr_ord_itms?id='+ord_id, 
    method: 'get',
  })
}

// Get the information of One order (No Detail)
export function getUserOneOrder(id) {
  return request({
    url:  BASE_URL + '/usr_one_ord?id='+id, //id: UserOrder.id
    method: 'get',
  })
}

// Similar to `getUserOneOrder`, Get all the orders (No Detail)
export function getUserAllOrders(usr_id) {
  return request({
    url:  BASE_URL + '/usr_all_ords?usr_id='+usr_id, 
    method: 'get',
  })
}



export function checkUserOneItem(data) {
  return request({
    url:  BASE_URL + '/check_usr_one_itm',
    method: 'put',
    data
  })
}

export function checkOrderPaid(data) {
  return request({
    url:  BASE_URL + '/check_ord_paid',
    method: 'put',
    data
  })
}

export function addUserOrderItem(data) {
  return request({
    url: BASE_URL + '/add_ord_itm',
    method: 'post',
    data
  })
}

export function deleteUserOrderItem(ord_itm_id) {
  return request({
    url: BASE_URL + '/delete_usr_one_itm?id='+ ord_itm_id,
    method: 'delete',
  })
}

export function deleteUserOrder(ord_id) {
  return request({
    url: BASE_URL + '/delete_usr_ord?id='+ ord_id,
    method: 'delete',
  })
}




// -========================== Admin Part ===========================

export function getAllUserOrdesr(id) {
  return request({
    url:  BASE_URL + '/all_usr_ords',
    method: 'get',
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