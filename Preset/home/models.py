from django.db import models
from merchan.models import Merchandise
from django.contrib.auth.models import User



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    merchan = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'User {self.customer.id} - {self.merchan.name} - {self.count}'
# Create your models here.
