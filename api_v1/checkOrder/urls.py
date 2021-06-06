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

    url('update_order', views.update_tag, name='updateTag'),
    url('update_order', views.update_order, name='updateOrder'),
    url('delete_one_tag', views.delete_one_tag, name='deleteOneTag'),
    url('delete_one_ord', views.delete_one_order, name='deleteOneOrder'),
    url('delete_all_ords', views.delete_all_orders, name='deleteAllOrders'),
]


#TODO:add_order() update.... delete......