from django.urls import path
from .views import CropView

urlpatterns = [
    path('crop/', CropView.as_view(), name='crop'),
]