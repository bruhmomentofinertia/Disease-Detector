from django.shortcuts import render
from .forms import RegionForm

# Create your views here.
def landing(request):
    context = {
      "form": RegionForm
    }
    return render(request, 'region/landing.html', context)