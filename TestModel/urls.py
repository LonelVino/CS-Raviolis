'''
/TestModel/urls.py
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/', views.testdb),
    path('/get', views.testdb_get),
    path('/post', views.testdb_post),
    path('/update', views.testdb_update),
    path('/delete', views.testdb_delete),
]