from django.shortcuts import render

# Create your views here.
from review.models import Review
from django.shortcuts import redirect
from .forms import UploadReviewForm

# Create your views here.

def uploadreview(request):
    if request.method=="POST":
        if form.is_valid():
            form.save()
    else:
        form = UploadReviewForm()
        return render(request,"review/reviewupload.html",{"form":form})

