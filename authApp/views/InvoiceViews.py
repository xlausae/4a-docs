from django.conf                                      import settings
from django.db.models                                 import query
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from authApp.models.product                           import Product
from authApp.serializers.invoiceSerializer            import InvoiceSerializer

class InvoiceCreateView(generics.CreateAPIView):
    serializer_class   = InvoiceSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        for sale in request.data["sales"]:
            product = Product.objects.get(id = sale["product"])
            if product.amount < sale["amount"]:
                stringResponse = {"detail":"Producto '" + product.name 
                + "' insuficiente para vender"}
                return Response(stringResponse, status=status.HTTP_406_NOT_ACCEPTABLE)


        serializer = InvoiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        for sale in request.data["sales"]:
            product = Product.objects.get(id = sale["product"])
            product.amount -= sale["amount"]
            product.save()
        
        return Response("Factura registrada ok", status=status.HTTP_201_CREATED)