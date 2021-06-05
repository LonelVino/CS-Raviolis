from django.conf.urls import url, include
from . import views


app_name='cart'
urlpatterns = [
    url('one_cart', views.one_cart, name='oneCartByUser'),   # ?usr_id=1
    # url('one_cart_item', views.one_cart_item, name='oneCartItemyUser'),   # ?cart_id=1
    url('cart_items', views.cart_items, name='CartItems'),   # ?cart_id=1
    url('add_cart', views.add_cart, name='addCart'),
    url('update_cart_item', views.update_cart_item, name='updateCartItem'), # {'quantity': 1}
    url('delete_cart', views.del_cart, name='delCart'), # cart?id
    url('delete_crt_item', views.del_cart_item, name='delCartItem'), # cart?id

    url('admin/all_carts', views.carts, name='allCarts'),       
]


#TODO:add_order() update.... delete......