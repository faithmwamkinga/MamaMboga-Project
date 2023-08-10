from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("name","email","phonenumber","location","id","password")
admin.site.register(Customer,CustomerAdmin)