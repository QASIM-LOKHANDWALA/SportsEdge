from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .api_functions import get_latest_news

def homepage(request):
  if request.user.is_authenticated:
    return render(request,'dashboard.html')
  else:
    return render(request,'home.html')

@login_required
def dashboard(request):
  news_data = get_latest_news()
  context = {"news_data":news_data}
  return render(request,'dashboard.html',context)