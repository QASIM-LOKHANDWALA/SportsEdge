from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
  if request.user.is_authenticated:
    return render(request,'dashboard.html')
  else:
    return render(request,'home.html')

@login_required
def dashboard(request):
  return render(request,'dashboard.html')