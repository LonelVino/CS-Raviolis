
from django.urls import path
from . import views

urlpatterns = [
    path('one_name', views.user_name),
    path('one_info', views.user_info),
    path('all_infos', views.all_user_infos),

    path('add_info', views.add_info),
    path('update_info', views.update_info),
    path('del_info', views.user_delete_byId),

    path('test_add', views.test_add),    
]