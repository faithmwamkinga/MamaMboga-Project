from django import forms
from models import Shipping

class UploadShipmentForm(model.ModelForm):
    model = shipmping
    class Meta:
        field = "__all__"