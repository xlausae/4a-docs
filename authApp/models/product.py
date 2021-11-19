from django.db import models


class Product(models.Model):
    id                = models.AutoField(primary_key=True)
    name              = models.CharField('Name',max_length = 30)
    price             = models.FloatField('Price')
    initial_stock     = models.IntegerField(default=0)
    stock_in          = models.IntegerField(default=0)
    stock_out         = models.IntegerField(default=0)
    final_stock       = models.IntegerField(default=0)
