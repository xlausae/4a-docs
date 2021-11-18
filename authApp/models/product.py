from django.db import models


class Product(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField('Name',max_length = 30)
    price     = models.FloatField('Price')
    amount    = models.IntegerField()