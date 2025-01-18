from django.shortcuts import render,HttpResponse
from .api_functions import Functions

# Create your views here.
def home(request):
  try:
    data = Functions.getTop10()
    print(data)
  except Exception as e:
    print(e)
  return HttpResponse('Chess')