from django.db import models

class Product(models.Model):
    name = models.CharField('Name of product',max_length=50)
    price = models.FloatField('Price')
    description = models.TextField('Description')
    count = models.IntegerField('Count')
    is_active = models.BooleanField('Available')
    categoryID = models.IntegerField('Category ID')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Category(models.Model):
    name = models.CharField('Name of category',max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'