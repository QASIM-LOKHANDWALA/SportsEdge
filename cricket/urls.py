from django.urls import path
from . import views

urlpatterns = [
  path('',view=views.cricket_home_page,name='cricket_home')
]
