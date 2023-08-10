from django.shortcuts import render
from shipmping.models import Shipping
from django.shortcuts import redirect
from .forms import UploadShipmentForm

# Create your views here.

def upload_shipment(request):
    if request.method=="POST":
        if form.is_valid()
        form.save()
    else:
        form=UploadShipmentForm
        return render(request,"shipping/shipmentupload.html",{"form":form})

