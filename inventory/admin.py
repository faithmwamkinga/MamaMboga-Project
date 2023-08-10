from django.contrib import admin

# Register your models here.
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","description","stock","date_created","date_updated")

admin.site.register(Products,ProductAdmin)    
# "image",