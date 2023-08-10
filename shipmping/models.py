# from django.db import models

# from order.models import Order

# # Create your models here.
# class Shipping(models.Model):
#     ship=models.OneToOneField.ForeignKey(Order,on_delete=models.CASCADE)
#     port_name=models.CharField(max_length=32)
#     customer_name=models.CharField(max_length=32)
#     phonenumber=models.CharField(max_length=16)
#     location=models.CharField(max_length=32)
#     product=models.CharField(max_length=32)
#     order=models.IntegerField()

#     def __str__(self):
#         return self.port_name


from django.db import models
# from order.models import Order

class Shipping(models.Model):
    # ship = models.OneToOneField(Order, on_delete=models.CASCADE)
    port_name = models.CharField(max_length=32)
    customer_name = models.CharField(max_length=32)
    phonenumber = models.CharField(max_length=16)
    location = models.CharField(max_length=32)
    product = models.CharField(max_length=32)
    # order = models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return self.port_name
