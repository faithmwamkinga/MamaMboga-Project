from django.urls import path
from .views import uploadcustomer
from django.conf import settings
from django.conf.urls.static import static
from .views import uploadcustomer

urlpatterns=[
    path("customer/upload",uploadcustomer, name="customeruploadview"),
 
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





