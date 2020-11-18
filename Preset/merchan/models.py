from django.db import models
from product.models import Product


class Merchandise(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    gender = models.CharField(max_length=64, null=True, blank=True)
    group = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
