from django.shortcuts import render
from .api_functions import CricketDataAPI

# Create your views here.
def cricket_home_page(request):
  try:
    cricket_api = CricketDataAPI()
    current_matches = cricket_api.get_current_matches()
    cricket_series = cricket_api.get_series()
    
    context = {
      'current_matches': current_matches,
      'cricket_series': cricket_series
    }
    return render(request, 'cricket_home.html', context)
    
  except Exception as e:
    context = {
      'error_message': str(e),
      'current_matches': [],
      'cricket_series': []
    }
    return render(request, 'cricket_home.html', context)