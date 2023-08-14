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

def cart_list(request):
    cart=Products.objects.all()
    return render(request,"inventory/cartlist.html",{"product":product})

def product_details(request,id):
    product=Products.objects.get(id=id)
    return render(request,"inventory/product_details.html",{"product":product})

def add_to_cart(request):
    cartitems=[]
    return render(request, "inventory/add_to_cart.html", {"cartitems":cartitems})

def edit_product_view(request,id):
    product=Products.objects.get(id=id)
    if request.method=='POST':
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("product_details_view",id=product.id)
    else:
        form = ProductUploadForm(instance=product)
        return render(request,"inventory/edit_product.html",{"form",form})





   