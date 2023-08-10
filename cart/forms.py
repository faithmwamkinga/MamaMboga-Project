from django import forms
from .models import Cart

class UploadCartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields = "__all__"


# from django import forms
# from .models import Products

# class ProductUploadForm(forms.ModelForm):
#     class Meta:
#         model=Products
#         fields="__all__"
