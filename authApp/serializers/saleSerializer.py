from authApp.models.sale import Sale
from rest_framework      import serializers

class SaleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ["product","amount","cost"]
