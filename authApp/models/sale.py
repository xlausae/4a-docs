from django.db import models
from .invoice import Invoice
from .product import Product

class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='sale',on_delete=models.SET_NULL,null=True)
    invoice = models.ForeignKey(Invoice, related_name='sale',on_delete=models.SET_NULL,null=True)
    paymentMethod = models.CharField('PaymentMethod', max_length = 30)
    amount= models.IntegerField()
    cost=models.FloatField('Cost',default=0)