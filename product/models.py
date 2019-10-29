from django.db import models
from brand.models import Brand

# Create your models here.

class Product(models.Model):
  product_name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=8,decimal_places=2)
  brand= models.ForeignKey(Brand ,on_delete=models.CASCADE)

  def __str__(self):
    return self.product_name

class Category(models.Model):
  category_name = models.CharField(max_length=50)
  product = models.ManyToManyField(Product)

  def __str__(self):
    return self.category_name
