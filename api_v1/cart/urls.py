from django.conf.urls import url, include
from . import views


app_name='cart'
urlpatterns = [
    url('cart', views.one_cart,
        name='oneCart'),   # cart?id
    url('all_carts', views.carts,
        name='allCarts'),       
    ]


#TODO:add_order() update.... delete......