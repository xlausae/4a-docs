from django.contrib import admin
from .models.invoice import Invoice
from .models.sale import Sale
from .models.user import User
from .models.account import Account
from .models.product import Product

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Invoice)
# Register your models here.
