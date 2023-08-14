from django import forms
from .models import Cart

class UploadCartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields = "__all__"
