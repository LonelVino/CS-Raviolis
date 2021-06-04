from django.conf.urls import url, include
from . import views


app_name='order'
urlpatterns = [
    url('order', views.one_order,
        name='oneOrder'),   # order?id
    url('all_orders', views.orders,
        name='allOrders'),   
    ]


#TODO:add_order() update.... delete......