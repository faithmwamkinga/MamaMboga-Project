from django.contrib import admin

# Register your models here.
from .models import Shipping
class ShippingAdmin(admin.ModelAdmin):
    list_display=("customer_name","port_name","phonenumber","location","product","order")
admin.site.register(Shipping,ShippingAdmin)