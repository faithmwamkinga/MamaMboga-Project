from django.contrib import admin

# Register your models here.
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display=("amount","date_created","receipt")
admin.site.register(Payment,PaymentAdmin)
