from django.shortcuts import render
from django.conf import settings
def graph_trends(symptom, areaCode):
  from pytrends.request import TrendReq
  import matplotlib.pyplot as plt

  # Create pytrends object and specify region and time period
  pytrends = TrendReq(hl='en-US', tz=360)
  pytrends.build_payload(kw_list=[symptom], timeframe='today 5-y',  geo='US-VA-' + str(areaCode))
  # Request data and extract values
  data = pytrends.interest_over_time().values[:, 0]

  # Plot data using matplotlib
  plt.plot(range(len(data)), data)
  plt.xlabel('Week')
  plt.ylabel('Search Trend')
  plt.savefig(areaCode + symptom + ".png")

def graphs(areaCode):
  symptoms = ['diarrhea', 'stomach cramps', 'vomiting', 'nausea', 'fever']
  for symptom in symptoms:
    graph_trends(symptom, areaCode)
  
# Create your views here.
def landing(request):
    return render(request, 'trending/landing.html')

def graph(request):
  inp_value = request.GET.get('sympt', 'default')
  if inp_value != 'default':
    context = {'code': inp_value,
              'symptoms': ['diarrhea', 'stomach cramps', 'vomiting', 'nausea', 'fever']
              }
    settings.AREA_CODE = inp_value
    return render( request, 'trending/graph.html', context)
  context = {
      'code': settings.AREA_CODE,
      'symptoms': ['diarrhea', 'stomach cramps', 'vomiting', 'nausea', 'fever']
    }
  return render(request, 'trending/graph.html', context)