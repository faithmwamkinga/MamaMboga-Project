from django import forms
from .models import Shipping

class UploadShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = "__all__"