from django.conf.urls import url, include
from . import views


app_name='order'
urlpatterns = [
    # --------------------- User Part ------------------------
    url('one_ord_itm', views.one_order_item, name='oneOrderItem'),   # order?id
    url('usr_one_ord', views.user_one_order, name='userOneOrder'),   # order?id
    url('usr_all_ords', views.user_all_orders, name='userAllOrders'),   # order?id
    url('usr_ord_itms', views.user_one_order_items, name='userOneOrderItems'),   # order?id
    
    url('check_usr_one_itm', views.check_user_one_item, name='checkUserOneItem'),
    url('check_usr_all_itms', views.check_user_all_items, name='checkUserAllItems'),
    
    url('add_ord_itm', views.add_order_item, name='addOrderItem'),
    url('delete_usr_one_itm', views.del_user_one_item, name='deleteUserOneOrderItem'),
    url('delete_usr_one_ord', views.delete_user_one_order, name='deleteUserOneOrder'),
    url('delete_usr_all_ords', views.delete_user_all_orders, name='deleteUserAllOrderItems'),

    # ---------------------- Admin Part -------------------------
    url('all_usrs_ords', views.all_users_orders, name='allUsersOrders'),      
    url('all_ord_itms', views.order_items, name='allOrderItems'),  

    url('update_one_usr_ord', views.order_items, name='updateOneUserOrder'),
    url('delete_all_usrs_ords', views.order_items, name='deleteAllUsersOrders'),
]


#TODO:add_order() update.... delete......