from django.db import models


# Create your models here.


class Iphone_Data(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    ratings = models.FloatField()
    reviews = models.PositiveSmallIntegerField()
