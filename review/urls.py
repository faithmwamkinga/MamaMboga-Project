from django.urls import path
from .views import uploadreview
from django.conf import settings

urlpatterns=[
    path("review/upload",uploadreview,name="review_upload_view")
]