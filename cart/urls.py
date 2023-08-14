from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import cart_upload,cart_list

urlpatterns=[
    path("cart/upload",cart_upload,name="cart_upload_view"),
    path("cart/cartlist",cart_list, name="product_list_view"),

]