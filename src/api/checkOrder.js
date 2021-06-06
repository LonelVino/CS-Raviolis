import request from '@/utils/request'

var BASE_URL = '/api_v1/check_order'
var ADMIN_BASE_URL = '/api_v1/check_order/admin'

// --------------------------------- User Part -----------------------
export function getOneCheckTag(id) {
  return request({
    url:  BASE_URL + '/one_tag?id='+id,  //id: checkTag.id
    method: 'get',
  })
}

// Get the realted order items according to the order_id
export function getAllCheckTags() {
  return request({
    url:  BASE_URL + '/all_tags', 
    method: 'get',
  })
}

// Get the information of One order (No Detail)
export function getOneCheckOrder(id) {
  return request({
    url:  BASE_URL + '/one_order?id='+id, //id: checkOrder.id
    method: 'get',
  })
}

// Similar to `getUserOneOrder`, Get all the orders (No Detail)
export function getAllCheckOrders(tag_id) {
  return request({
    url:  BASE_URL + '/all_orders?tag_id='+tag_id, 
    method: 'get',
  })
}


export function addCheckTag(data) {
    return request({
      url: BASE_URL + '/add_tag',
      method: 'post',
      data
    })
  }

export function addCheckOrder(data) {
  return request({
    url: BASE_URL + '/add_order',
    method: 'post',
    data
  })
}

export function checkOneOrder(data) {
    return request({
      url:  BASE_URL + '/check_one_ord',
      method: 'put',
      data
    })
  }


export function addOrderQuantity(data) {
  return request({
    url:  BASE_URL + '/add_ord_quan',
    method: 'put',
    data
  })
}

export function updateTag(data) {
  return request({
    url:  BASE_URL + '/update_tag',
    method: 'put',
    data
  })
}

export function updateOrder(data) {
  return request({
    url:  BASE_URL + '/update_order',
    method: 'put',
    data
  })
}


export function deleteOneTag(tag_id) {
  return request({
    url: BASE_URL + '/delete_one_tag?id='+ tag_id,
    method: 'delete',
  })
}

export function deleteOneOrder(ord_id) {
  return request({
    url: BASE_URL + '/delete_one_ord?id='+ ord_id,
    method: 'delete',
  })
}

// This will delete all orders buut won't delete the tag
export function deleteAllOrders(tag_id) {
  return request({
    url: BASE_URL + '/delete_all_ords?id='+ tag_id,
    method: 'delete',
  })
}







// -========================== Admin Part ===========================
