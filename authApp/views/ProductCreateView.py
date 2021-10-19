from django.conf                                      import settings
from django.db.models import query
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from authApp.models.product                    import Product
from authApp.serializers.productSerializer    import ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    serializer_class   = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        
        serializer = ProductSerializer(data=request.data['product_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response("Producto agregado exitosamente", status=status.HTTP_201_CREATED)





