# coding: utf-8
from django.db import models
from ierg4210Be.settings import HOST_DEV
from tools import TimeHandle


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Productions(models.Model):
    name = models.CharField(max_length=100, blank=True)
    category_id = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    Image = models.FileField(upload_to='./static/upload/pic/', blank=True)

    def __unicode__(self):
        return self.name

    def get_production(self):
        return {
            "id": self.id,
            "name": self.name,
            "category_id": self.category_id,
            "price": self.price,
            "description": self.description,
            "image": HOST_DEV + self.Image.url[13:],
        }


class Bill(models.Model):
    series = models.CharField(max_length=100, blank=True)
    create_time = models.CharField(max_length=30, blank=True)
    state = models.IntegerField(default=-1)  # -1: 未产生 1: 未支付 2 已支付 3: 已退货
    user_id = models.IntegerField(default=-1)

    def get_bill(self):
        return {
            "id": self.id,
            "bill_series": self.series,
            "create_time": self.create_time,
        }


class ProductionInBill(models.Model):
    production_id = models.IntegerField(default=-1)
    bill_id = models.IntegerField(default=-1)

    def get_production_in_bill(self):
        return {
            "nexus_id": self.id,
            "production_id": self.production_id,
            "bill_id": self.bill_id,
        }


class User(models.Model):
    email = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)  # password 要加盐处理
    session_id = models.CharField(max_length=1000, blank=True)  # 后期把session放到缓存里面

    def get_user(self):
        return {
            "id": self.id,
            "email": self.email,
            "nickname": self.nickname,
            "password": self.password,
        }


class ShoppingCart(models.Model):
    user_id = models.IntegerField(default=-1, unique=True)

    def get_shopping_cart(self):
        return {
            "shopping_cart_id": self.id,
            "user_id": self.user_id,
        }


class ProductionInShoppingCart(models.Model):
    production_id = models.IntegerField(default=-1)
    shopping_cart_id = models.IntegerField(default=-1)

    def get_production_in_shopping_cart(self):
        return {
            "nexus_id": self.id,
            "production_id": self.production_id,
            "shopping_cart_id": self.shopping_cart_id,
        }
# Create your models here.
