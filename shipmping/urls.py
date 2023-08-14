from django.urls import path
from .views import upload_shipment
from django.conf import settings

urlpatterns=[
    path("shipmping/upload",upload_shipment,name="shipment_upload_view")
]
