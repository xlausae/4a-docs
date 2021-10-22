from rest_framework         import serializers
from authApp.models.invoice import Invoice

class invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model: Invoice
        fields=['date','user', 'paymentMethod']
    def to_representation(self, obj):
        invoice= Invoice.objects.get(id=obj.id)

        return {
            'date':invoice.date,
            'user':invoice.user,
            'paymentMethod':invoice.paymentMethod

        }