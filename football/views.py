from django.http import JsonResponse
from django.shortcuts import render
from .api_functions import get_leagues, search_leagues, get_league_details, get_league_standings, get_top_scorers
from .models import Player
from django.contrib.auth.decorators import login_required

FAMOUS_PLAYERS = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappe", "Kevin De Bruyne"]

@login_required(login_url='login')
def football_home_page(request):
    data = get_leagues()
    top_earning_players = Player.objects.order_by('-wage_euro')[:6]

    context = {
        'leagues': data.get('response', []),
        'famous_players': top_earning_players
    }
    return render(request, 'football/football_home.html', context)

  
def search_league_view(request):
    query = request.GET.get("q", "")
    results = search_leagues(query)
    return JsonResponse({"leagues": results})
  
def league_details_view(request, league_id):
    league = get_league_details(league_id)
    if league:
        season = league.get("seasons", [])[-1] if league.get("seasons") else None
        standings = get_league_standings(league_id, season["year"]) if season else []
        top_scorers = get_top_scorers(league_id, season["year"]) if season else []
    else:
        season, standings, top_scorers = None, [], []
    return render(request, 'football/league_details.html', {
        "league": league,
        "season": season,
        "standings": standings,
        "top_scorers": top_scorers
    })
    
def search_player_view(request):
    query = request.GET.get("q", "")
    if query:
        results = Player.objects.filter(full_name__icontains=query)
    else:
        results = Player.objects.none()
    
    return JsonResponse({"players": list(results.values("full_name", "age", "nationality", "overall_rating"))})
