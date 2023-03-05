from django.shortcuts import render
from django.conf import settings

# Create your views here.
def landing(request):
  inp_value = request.GET.get('uname', 'default')
  if inp_value != 'default':
    context = {'region': inp_value}
    settings.USERNAME = inp_value
    return render( request, 'graph/landing.html', context)
  context = {
      'region': settings.USERNAME,
    }
  return render(request, 'graph/landing.html', context)
