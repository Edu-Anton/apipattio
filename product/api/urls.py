from django.conf.urls import url
from django.contrib import admin

from .views import (
  ProductListAPIView,
  ProductDetailAPIView,
  CategoryListAPIView,
)

urlpatterns = [
  url( 'category', CategoryListAPIView.as_view(), name='category_list'),
  url( '', ProductListAPIView.as_view(), name='list'),
  url( 'product_detail/<int:pk>', ProductDetailAPIView.as_view(), name='product_detail'),
]