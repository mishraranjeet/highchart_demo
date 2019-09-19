from django.db import models
import csv


# Create your models here.


class Iphone_Data(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    ratings = models.FloatField()
    reviews = models.PositiveSmallIntegerField()

#below code run only one time to save the data to database
# with open('iphone_data.csv') as csvfile:
#     data_read = csv.DictReader(csvfile)
#     for row in data_read:
#         p = Iphone_Data(product_name=row['ProductName'], price=row['Price'], ratings=row['Ratings'],
#                         reviews=row['Reviews'])
#         p.save()
