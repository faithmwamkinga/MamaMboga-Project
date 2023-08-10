from django.contrib import admin

# Register your models here.
from .models import Review
class ReviewAdmin(admin.ModelAdmin):
    list_display=("sender_name","title","description","message","time_and_date")
admin.site.register(Review,ReviewAdmin)
