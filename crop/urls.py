from django.urls import path
from .views import CropView

urlpatterns = [
    path('crops', CropView.as_view(), name='crops'),
]