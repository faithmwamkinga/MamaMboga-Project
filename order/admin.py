from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("order_name","order_id","date_created","date_updated","order_status","number_of_orders","stock_amount")
admin.site.register(Order,OrderAdmin)



