from authApp.models.product import Product
from rest_framework         import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','initial_stock','stock_in', 'stock_out','final_stock']

    def to_representation(self, obj):
        
        product = Product.objects.get(id=obj.id)

        return {
            'id'     : product.id,
            'name'   : product.name,
            'price'  : product.price,
            'initial_stock' : product.initial_stock,
            'stock_in'      : product.stock_in,
            'stock_out'     : product.stock_out,
            'final_stock'   : product.final_stock
        }