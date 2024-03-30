from rest_framework import status, viewsets
from product.models import Product
from product.serializers import ProductSerializer

# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer