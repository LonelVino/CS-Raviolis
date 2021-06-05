from django.contrib import admin
from api_v1.user import models as user_models
from api_v1.cart import models as cart_models
from api_v1.shop import models as shop_models
from api_v1.order import models as order_models

# Register your models here.
admin.site.register(user_models.User)
admin.site.register(cart_models.Cart)
admin.site.register(cart_models.CartItem)
admin.site.register(shop_models.Product)
admin.site.register(shop_models.Category)
admin.site.register(order_models.UserOrder)
admin.site.register(order_models.OrderItem)
