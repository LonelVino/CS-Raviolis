"""cs_raviolis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('api_v1/', include('api_v1.urls')),
    path('api_v1/user/', include('api_v1.user.urls')),
    path('api_v1/shop/', include('api_v1.shop.urls')),
    path('api_v1/cart/', include('api_v1.cart.urls')),
    path('api_v1/order/', include('api_v1.order.urls')),
    path('api_v1/check_order/', include('api_v1.checkOrder.urls')),

    path('testdb/', include('TestModel.urls'), name='testdb'),

]
