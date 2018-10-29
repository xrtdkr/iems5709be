from django.contrib import admin
from be.models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class ProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'price', 'description')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Productions, ProductionAdmin)

# Register your models here.
