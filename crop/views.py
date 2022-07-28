from django.shortcuts import render
from django.views import View

from .models import CropModel


# Create your views here.
#  get all crops class view
class CropView(View):
    def get(self, request):
        crop = CropModel.objects.all()
        return render(request, 'crop.html', {'crops': crops})

    def post(self, request):
        # svae CropModel data
        crop = CropModel(
            name=request.POST['name'],
            created_at=request.POST['created_at'],
            updated_at=request.POST['updated_at'],
        )
        crop.save()
        return render(request, 'crop.html', {'crops': CropModel.objects.all()})