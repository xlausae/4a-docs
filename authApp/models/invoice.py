from django.db import models
from .user import User

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    user = models.ForeignKey(User, related_name='invoice',on_delete=models.SET_NULL,null=True)
    paymentMethod = models.CharField('PaymentMethod', max_length = 30)