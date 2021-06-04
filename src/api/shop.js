import request from '@/utils/request'

var BASE_URL = '/api_v1/shop'
var ADMIN_BASE_URL = '/api_v1/shop/admin'


export function getCat(id, slug) {
  return request({
    url:  BASE_URL + '/category?id='+id +'&slug=' + slug,
    method: 'get',
  })
}

export function getAllCats() {
  return request({
    url: BASE_URL + '/all_categories',
    method: 'get',
  })
}

export function getProd(id, slug) {
  return request({
    url:  BASE_URL + '/product?id='+id +'&slug=' + slug,
    method: 'get',
  })
}

export function getAllProds() {
  return request({
    url: BASE_URL + '/all_prods',
    method: 'get',
  })
}


// --------------- AMDIN PART -----------------------

export function addCat(data) {
  return request({
    url: ADMIN_BASE_URL + '/add_cat',
    method: 'post',
    data
  })
}

export function addProd(data) {
  return request({
    url: ADMIN_BASE_URL + '/add_prod',
    method: 'post',
    data
  })
}

export function updateCat(data) {
  return request({
    url: ADMIN_BASE_URL + '/update_cat',
    method: 'put',
    data
  })
}

export function updateProd(data) {
  return request({
    url: ADMIN_BASE_URL + '/update_prod',
    method: 'put',
    data
  })
}

export function deleteCat(id) {
  return request({
    url: ADMIN_BASE_URL + '/del_cat?id='+id,
    method: 'delete',
  })
}

export function deleteProd(id) {
  return request({
    url: ADMIN_BASE_URL + '/del_prod?id='+id,
    method: 'delete',
  })
}