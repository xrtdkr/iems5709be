from django.contrib import admin
from be.models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class ProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'price', 'description')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname', 'password', 'session_id', 'is_super')


class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'series', 'create_time', 'state', 'user_id')


class ProductionInBillAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_id', 'bill_id')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id')


class ProductionInShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_id', 'shopping_cart_id')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Productions, ProductionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(ProductionInBill, ProductionInBillAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(ProductionInShoppingCart, ProductionInShoppingCartAdmin)
# Register your models here.
