from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=150)
    about = models.TextField(max_length=2048)
    max_presets = models.IntegerField(default=10)
    is_discount_preset = models.BooleanField(default=True)

    def __str__(self):
        return f'Product - {self.name}'
