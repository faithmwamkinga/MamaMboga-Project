from django.urls import path
from .views import upload_product,product_list,product_details,add_to_cart,edit_product_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("products/upload",upload_product,name="product_upload_view"),
    path("products/productslist",product_list, name="product_list_view"),
    path("products/<int:id>/", product_details, name="product_details_view"),
    path("products/add_to_cart", add_to_cart, name="add_to_cart_view"),
    path("products/edit/<int:id>/", edit_product_view, name= "product_edit_view"),
 
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)