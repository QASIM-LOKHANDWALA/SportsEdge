from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .data_structure import CricketDataManager
from django.http import JsonResponse
from .models import CricketPlayer
from django.contrib.auth.decorators import login_required
from datetime import date

POPULAR_CRICKET_PLAYERS = [
    "Virat Kohli",
    "Babar Azam",
    "Joe Root",
    "Rohit Sharma",
    "Kane Williamson",
    "Ben Stokes"
]

@login_required(login_url='login')
def cricket_home_page(request):
    cricket_manager = CricketDataManager()
    data = cricket_manager.refresh_data()

    famous_players = CricketPlayer.objects.filter(fullname__in=POPULAR_CRICKET_PLAYERS)

    for player in famous_players:
        if player.date_of_birth:
            player.age = date.today().year - player.date_of_birth.year
        else:
            player.age = "N/A"

    context = {
        'current_matches': data['matches'], 
        'cricket_series': data['series'],  
        'famous_players': famous_players  
    }
    return render(request, 'cricket/cricket_home.html', context)


def search_player(request):
    query = request.GET.get('q', '').strip()
    if query:
        players = CricketPlayer.objects.filter(fullname__icontains=query).values(
            'id', 'fullname', 'image_path', 'country_name', 'country_image_path',
            'position', 'batting_style', 'bowling_style', 'date_of_birth'
        )[:10] 

        for player in players:
            if player["date_of_birth"]:
                player["age"] = date.today().year - player["date_of_birth"].year
            else:
                player["age"] = "N/A"

        return JsonResponse({'players': list(players)})
    
    return JsonResponse({'players': []})
