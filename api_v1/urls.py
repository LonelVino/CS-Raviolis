'''
/api_v1/urls.py
-------------------------
Organize the api urls of parts: user, cart, order, shop
'''

from django.urls import path
from . import views

urlpatterns = [
    path('/', views.pages),
]