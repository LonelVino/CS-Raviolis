from django.contrib import admin

from .models import Cart, CartItem

# 内置的表
class CartItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']


class CartAdmin(admin.ModelAdmin):
    list_display = ['username','get_total_cost','created']
    list_filter = ['created', 'updated']
    inlines = [CartItemInline]

class CartItemAdmin(admin.ModelAdmin):
    list_display =['product','quantity','get_cost']
    list_filter = ['product']



admin.site.register(Cart, CartAdmin)

admin.site.register(CartItem, CartItemAdmin)
