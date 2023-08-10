from django.db import models
from inventory.models import Products
from customer.models import Customer
# from order.models import Order
class Cart(models.Model):
    # Product=models.ManyToManyField(Product)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    number = models.PositiveIntegerField
    size = models.PositiveIntegerField()
    def str(self):
        return self.number
