from django.conf.urls import url, include
from . import views


app_name='checkOrder'
urlpatterns = [
    url('one_tag', views.one_tag, name="oneTag"),
    url('all_tags', views.all_tags, name="allTags"),
    url('one_order', views.one_order, name="oneOrder"),
    url('all_orders', views.all_orders, name="allOrders"),
    url('add_tag', views.add_tag, name='addTag'),  
    url('add_order', views.add_order, name='addOrder'),  

    url('check_one_ord', views.check_one_order, name="checkOneOrder"),
    url('add_ord_quan', views.add_order_quantity, name="addOrderQuantity"),

    url('update_tag', views.update_tag, name='updateTag'),
    url('update_order', views.update_order, name='updateOrder'),
    url('delete_one_tag', views.delete_one_tag, name='deleteOneTag'),
    url('delete_one_ord', views.delete_one_order, name='deleteOneOrder'),
    url('delete_all_ords', views.delete_all_orders, name='deleteAllOrders'),
]


#TODO:add_order() update.... delete......