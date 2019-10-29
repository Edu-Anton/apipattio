from rest_framework import generics

from brand.models import Brand
from product.models import Product
from brand.api.serializers import BrandSerializer
from product.api.serializers import ProductSerializer

class BrandList(generics.ListAPIView):
  queryset = Brand.objects.all()
  serializer_class = BrandSerializer

class BrandDetail(generics.RetrieveDestroyAPIView):
  queryset = Brand.objects.all()
  serializer_class = BrandSerializer

# class BrandProductsList(generics.ListCreateAPIView):
#     def get_queryset(self):
#         queryset = .objects.filter(category_id=self.kwargs['pk'])
#         return queryset
#     serializer_class = SubCategorySerializer

class BrandProductsList(generics.ListAPIView):
  def get_queryset(self):
    queryset = Product.objects.filter(brand_id=self.kwargs['pk'])
    return  queryset
  serializer_class = ProductSerializer
