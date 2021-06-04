from django.contrib import admin

from .models import UserOrder, OrderItem,

# 内置的表
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class UserOrderAdmin(admin.ModelAdmin):
    list_display = ['username','get_total_cost','created']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    list_display =['product','quantity','get_cost']
    list_filter = ['product']



admin.site.register(UserOrder, UserOrderAdmin)

admin.site.register(OrderItem, OrderItemAdmin)
