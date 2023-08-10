from django import forms
from .models import Payment

class UploadPaymentForms(forms.ModelForm):
    class Meta:
        model = Payment
        field = "__all__"
