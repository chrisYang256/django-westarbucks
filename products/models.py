from django.db import models

# Create your models here.
class Menu(models.Model):
  name = models.CharField(max_length=45, null=True)

  class Meta:
    db_table = 'menus'


class Category(models.Model):
  name = models.CharField(max_length=45, null=True)
  menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null=True)

  class Meta:
    db_table = 'categories'


class Product(models.Model):
  korean_name = models.CharField(max_length=45, null=True)
  english_name = models.CharField(max_length=45, null=True)
  description = models.TextField(default="")
  category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
  nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE, null=True)

  class Meta:
    db_table = 'products'


class Image(models.Model):
  image_url = models.CharField(max_length=2000, null=True)
  product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)

  class Meta:
    db_table = 'images'


class Nutrition(models.Model):
  one_serving_kca = models.DecimalField(default=0, max_digits=6, decimal_places=2)
  sodium_mg = models.DecimalField(default=0, max_digits=6, decimal_places=2)
  saturated = models.DecimalField(default=0, max_digits=6, decimal_places=2)
  sugars_g = models.DecimalField(default=0, max_digits=6, decimal_places=2)
  protein_g = models.DecimalField(default=0, max_digits=6, decimal_places=2)
  caffeine_mg = models.DecimalField(default=0, max_digits=6, decimal_places=2)
  size_ml = models.CharField(max_length=45, null=True)
  size_fluid_ounce = models.CharField(max_length=45, null=True)

  class Meta:
    db_table = 'nutritions'


class Allergy(models.Model):
  name = models.CharField(max_length=45, null=True)
  products = models.ManyToManyField(Product)

  class Meta:
    db_table = 'allergies'