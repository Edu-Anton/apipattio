from rest_framework.serializers import ModelSerializer
from brand.models import Brand

class BrandSerializer(ModelSerializer):
  class Meta:
    model = Brand
    fields = ['id', 'brand_name']