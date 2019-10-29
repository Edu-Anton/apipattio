from rest_framework.generics import ListAPIView, RetrieveAPIView

from product.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductListAPIView(ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class CategoryListAPIView(ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer