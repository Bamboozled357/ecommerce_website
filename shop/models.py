
from django.db import models

from account.models import MyUser


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    profile = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    profile = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"

