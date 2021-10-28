from rest_framework         import serializers
from authApp.models.invoice import Invoice
from authApp.models.sale    import Sale
from authApp.serializers.saleSerializer import SaleSerializer

class InvoiceSerializer(serializers.ModelSerializer):

    sales = SaleSerializer(many=True)

    class Meta:
        model  = Invoice
        fields = ["id","date","user","paymentMethod","sales"]

    def create(self,validated_data):

        listSaleData    = validated_data.pop("sales")
        invoiceInstance = Invoice.objects.create(**validated_data)
        
        for saleData in listSaleData:
            Sale.objects.create(invoice=invoiceInstance,**saleData)
        return invoiceInstance