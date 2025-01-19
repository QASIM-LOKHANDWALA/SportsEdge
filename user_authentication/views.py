from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django import forms

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
      user = form.save()
      login(request,user)
      return 'Success'
  else:
    form = CustomUserCreationForm()
  return render(request, 'user_authentication/register.html', {'form': form})

def login_view(request):
  pass

def logout_view(request):
  pass