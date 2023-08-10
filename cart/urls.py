from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import cart_upload

urlpatterns=[
    path("cart/upload",cart_upload,name="cart_upload_view")

]