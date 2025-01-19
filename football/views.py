from django.shortcuts import render,HttpResponse
from .api_functions import get_leagues

# Create your views here.
def homepage(request):
  data = get_leagues()
  print(data)
  return HttpResponse('Football')