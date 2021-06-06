import request from '@/utils/request'

var CAS_BASE_URL = '/api_v1/cas'

var BASE_URL = '/api_v1/user'

export function register(data) {
  return request({
    url: CAS_BASE_URL + '/register',
    method: 'post',
    data
  })
}

export function login(data) {
  return request({
    url: CAS_BASE_URL + '/login',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: CAS_BASE_URL + '/logout',
    method: 'post'
  })
}

export function getRole(cas_id) {
  return request({
    url: CAS_BASE_URL + '/get_role?cas_id=' + cas_id,
    method: 'get',
  })
}

export function getName(id) {
  return request({
    url: BASE_URL + '/one_name?id=' + id,
    method: 'get',
  })
}

export function getInfo(id, name) {
  return request({
    url:  BASE_URL + '/one_info?id='+id +'&name=' + name,
    method: 'get',
  })
}

export function getAllInfos() {
  return request({
    url: BASE_URL + '/all_infos',
    method: 'get',
  })
}

export function addInfo(data) {
  return request({
    url: BASE_URL + '/add_info',
    method: 'post',
    data
  })
}

export function updateInfo(data) {
  return request({
    url: BASE_URL + '/update_info',
    method: 'put',
    data
  })
}

export function deleteInfo(id) {
  return request({
    url: BASE_URL + '/del_info?id='+id,
    method: 'delete',
  })
}