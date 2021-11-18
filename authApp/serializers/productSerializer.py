from authApp.models.product import Product
from rest_framework         import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','amount']

    def to_representation(self, obj):
        
        product = Product.objects.get(id=obj.id)

        return {
            'id'     : product.id,
            'name'   : product.name,
            'price'  : product.price,
            'amount' : product.amount
        }