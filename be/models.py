from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return self.name


class Productions(models.Model):
    name = models.CharField(max_length=100, blank=True)
    category_id = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name


class Bill(models.Model):
    pass


class ProductionInBill(models.Model):
    pass

# Create your models here.
