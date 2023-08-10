from django.shortcuts import render
from .forms import UploadCustomerForm
from customer.models import Customer
from django.shortcuts import redirect

# Create your views here.

def uploadcustomer(request):
    if request.method=="POST":
        form=UploadCustomerForm(request.POST,request.Files)
        if form.is_valid():
            forms.save()
    else:
        form = UploadCustomerForm()
        return render(request,"customer/customerupload.html",{"form":form})
