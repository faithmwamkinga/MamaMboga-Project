from django.shortcuts import render
from payment.models import Payment
from django.shortcuts import redirect
from .forms import UploadPaymentForms

# Create your views here.

def uploadpayment(request):
    if request.method=="POST":
        if form.is_valid():
            form.save()
    else:
        form = UploadPaymentForms()
        return render(request,"payment/paymentupload.html",{"form":form})

