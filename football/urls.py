from django.urls import path
from .views import football_home_page, search_league_view, league_details_view,search_player_view

urlpatterns = [
    path('', football_home_page, name='football_home'),
    path('search/', search_league_view, name='search_league'),
    path('league/<int:league_id>/', league_details_view, name='league_details'),
    path('search_player/', search_player_view, name='search_player'),
]