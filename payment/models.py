from django.db import models

# from order import Order
# Create your models here.
class Payment(models.Model):
    amount=models.IntegerField()
    date_created=models.DateField()
    # pending_payment=models.CharField(max_length=32)
    receipt=models.CharField(max_length=32)
    payment_methods=models.CharField(max_length=32)
    
    def __str__(self):
        return self.receipt


