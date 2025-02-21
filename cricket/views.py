from django.shortcuts import render
from .data_structure import CricketDataManager

def cricket_home_page(request):
    cricket_manager = CricketDataManager()
    data = cricket_manager.refresh_data()
    
    context = {
        'current_matches': data['matches'],
        'cricket_series': data['series']
    }
    
    return render(request, 'cricket/cricket_home.html', context)