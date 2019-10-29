from django.db import models

# Create your models here.
class Brand(models.Model):
  brand_name = models.CharField(max_length=50)
  ruc = models.CharField(max_length=11)

  def __str__(self):
    return '{}'.format(self.brand_name)

# class Influencer(models.Model):
