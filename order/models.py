from django.db import models
from payment.models import Payment
from shipmping.models import Shipping
from customer.models import Customer
# from cart.models import Cart
from shipmping.models import Shipping
from django.db import migrations


class Order(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, null=True)
    shipping = models.OneToOneField(Shipping, on_delete=models.PROTECT, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    # cart = models.OneToOneField(Cart, on_delete=models.PROTECT, null=True)
    order_name = models.CharField(max_length=32)
    order_id = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=32)
    number_of_orders = models.IntegerField(null=True)
    stock_amount = models.IntegerField()

    def __str__(self):
        return self.order_status

# class Migration(migrations.Migration):

#     dependencies = [
#     ]

#     operations = [
#         migrations.AddField(
#             model_name='order',
#             name='number_of_orders',
#             field=models.IntegerField(default=0),
#         ),
#         migrations.RunPython(set_default_number_of_orders),
#     ]
