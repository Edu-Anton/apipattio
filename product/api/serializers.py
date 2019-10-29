from rest_framework.serializers import ModelSerializer

from product.models import Product, Category

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = [ 'product_name', 'price', 'brand_id' ]

class CategorySerializer(ModelSerializer):
  class Meta:
    model = Category
    fields = ['category_name']