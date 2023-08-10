from django.shortcuts import render
from .forms import UploadCartForm
from django.shortcuts import redirect


# Create your views here.
def cart_upload(request):
    if request.method=="POST":
        form = UploadCartForm(request.POST,request.Files)
        if form.is_valid():
            forms.save()
    else:
        form = UploadCartForm()
        return render(request,"cartupload.html",{"form":form})



   