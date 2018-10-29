from django.db import models


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
    Image = models.FileField(upload_to='/upload/pic/')

    def __unicode__(self):
        return self.name

    def get_production(self):
        return {
            "id": self.id,
            "name": self.name,
            "category_id": self.category_id,
            "price": self.price,
            "description": self.description,
        }


class Bill(models.Model):
    pass


class ProductionInBill(models.Model):
    pass

# Create your models here.
