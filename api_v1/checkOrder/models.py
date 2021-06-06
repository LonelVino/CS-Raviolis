from django.db import models
from django.db.models.deletion import CASCADE
from api_v1.shop.models import Product

# related_name, items.all()
class checkTag(models.Model):
    name = models.CharField(max_length=100, default='None')
    created = models.CharField(max_length=100, default='None')
    ended = models.CharField(max_length=100, default='None')
    # 这个很有帮助，这样一来用Queryset取值的时候是按照先后顺序来的 
    class Meta:
        ordering = ('-created',)
        db_table = 'checkTag'

    def __str__(self):
        return 'checkTag {}'.format(self.id)

    # 在html中似乎不能调用related_name
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    get_total_cost.short_description='usr_price'

# 对应一个order
class checkOrder(models.Model):
    tag = models.ForeignKey(checkTag, related_name='check_order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='check_order',on_delete=models.CASCADE)
    itm_price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    gotten = models.BooleanField(default=False)
    product_name = models.CharField(max_length=100, default='None')
    category_name = models.CharField(max_length=100, default='None')
    # 应该直接加一项total_cost,方便之后直接用数据库统计,
    # 需要改orderItem的创建方式,以及最好order的也改，不过其实问题不大
    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.itm_price * self.quantity
    get_cost.short_description='cost'

    class Meta:
        db_table = 'checkOrder'
