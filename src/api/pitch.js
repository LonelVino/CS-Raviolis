import request from '@/utils/request'

var BASE_URL = '/django_api/pitch'


export function getScore(id, name) {
  return request({
    url:  BASE_URL + '/one_score?id='+id +'&name=' + name,
    method: 'get',
  })
}

export function getAllScores() {
  return request({
    url: BASE_URL + '/all_scores',
    method: 'get',
  })
}

export function addScore(data) {
  return request({
    url: BASE_URL + '/add_score',
    method: 'post',
    data
  })
}

export function updateScore(data) {
  return request({
    url: BASE_URL + '/update_score',
    method: 'put',
    data
  })
}

export function deleteScore(id) {
  return request({
    url: BASE_URL + '/del_score?id='+id,
    method: 'delete',
  })
}