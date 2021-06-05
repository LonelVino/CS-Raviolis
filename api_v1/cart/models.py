from django.db import models
from api_v1.shop.models import Product
from api_v1.user.models import User
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    ttl_price = models.FloatField(default=0.)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Cart'
        ordering = ('-created',)

    def __str__(self):
        return 'Cart {}'.format(self.id)

    # 在html中似乎不能调用related_name
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    get_total_cost.short_description='ttl_price'

# belong to a cart of one user
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    itm_price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'CartItem'

    def __str__(self):
        return 'CartItem {}'.format(self.id)

    def get_cost(self):
        return self.itm_price * self.quantity
    get_cost.short_description='cost'