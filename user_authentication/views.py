from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib import messages

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'})
  )
  password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
  )
  password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
  )

def register_view(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = CustomUserCreationForm()
  return render(request, 'user_authentication/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'Invalid username or password.')
  return render(request, 'user_authentication/login.html')

def logout_view(request):
  logout(request)
  return redirect('login')