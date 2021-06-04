from django.conf.urls import url, include
from . import views


app_name='order'
urlpatterns = [
    url('order', views.one_order, name='oneOrder'),   # order?id
    url('all_ords', views.orders, name='allOrders'),   
    url('order_item', views.one_order_item, name='oneOrderItem'),   # order?id
    url('all_ord_itms', views.order_items, name='allOrderItems'),  
    ]


#TODO:add_order() update.... delete......