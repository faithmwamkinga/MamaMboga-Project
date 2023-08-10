# from django.db import models

# # Create your models here.

# from order.models import Order
# class Customer(models.Model):
#     name=models.CharField(max_length=32)
#     email=models.CharField(max_length=32)
#     phonenumber=models.CharField(max_length=16)
#     location=models.CharField(max_length=32)
#     password=models.CharField(max_length=8)
#     user=models.ForeignKey(Order,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phonenumber = models.CharField(max_length=16)
    location = models.CharField(max_length=32)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name
