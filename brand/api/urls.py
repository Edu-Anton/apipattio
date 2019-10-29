from django.conf.urls import url
from django.urls import path
# from django.contrib import admin

from brand.api.views import (
  BrandList,
  BrandDetail,
  BrandProductsList,
)

urlpatterns = [
  path( '', BrandList.as_view(), name='brand_list'),
  path( '<int:pk>', BrandDetail.as_view(), name='brand_detail'),
  path('<int:pk>/products', BrandProductsList.as_view(), name='brand_products_list'),
  # path('v1/products/', ProductList.as_view(), name='product_list'),
  # path('v1/products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]