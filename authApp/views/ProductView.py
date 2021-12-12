from django.conf                                      import settings
from django.db.models import query
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from authApp.models.product                    import Product
from authApp.serializers.productSerializer     import ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    serializer_class   = ProductSerializer
    

    def post(self, request, *args, **kwargs):
        
        serializer = ProductSerializer(data=request.data['product_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response("Producto agregado exitosamente", status=status.HTTP_201_CREATED)


class ProductReadView(generics.ListAPIView):
    serializer_class   = ProductSerializer

    def get_queryset(self):
        
        queryset = Product.objects.all()
        return queryset

class ProductUpdateView(generics.UpdateAPIView):
    serializer_class   = ProductSerializer
    queryset           = Product.objects.all()

    def update(self, request, *args, **kwargs):
        
        return super().update(request, *args, **kwargs)

class ProductDeleteView(generics.DestroyAPIView):
    serializer_class   = ProductSerializer 
    queryset           = Product.objects.all()

    def delete(self, request, *args, **kwargs):
        
        return super().destroy(request, *args, **kwargs)