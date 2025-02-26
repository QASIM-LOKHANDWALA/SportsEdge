from django.urls import path
from . import views

urlpatterns = [
  path('', views.cricket_home_page, name='cricket_home'),
  path('search_player/', views.search_player, name='search_player'),
]
