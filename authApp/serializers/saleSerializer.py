from rest_framework         import serializers
from authApp.models.sale    import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model: Sale
        Fields=['product','invoice', 'paymentMetho','amount' ]

    def to_representation(self, obj):
        sale: Sale.objects.get(id=obj.id)

        return {
            'product':sale.product,
            'invoice':sale.invoice,
            'paymentMetho': sale.paymentMetho,
            'amount':sale.amount

        }
