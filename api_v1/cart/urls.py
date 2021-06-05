from django.conf.urls import url, include
from . import views


app_name='cart'
urlpatterns = [
    url('one_cart', views.one_cart, name='oneCartByUser'),   # cart?id
    url('add_cart', views.add_cart, name='addCart'),
    url('delete_cart', views.del_cart, name='delCart'), # cart?id
    url('update_cart', views.update_cart, name='updateCart'),
    url('admin/all_carts', views.carts, name='allCarts'),       
]


#TODO:add_order() update.... delete......