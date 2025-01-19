from django.shortcuts import redirect

def check_authenticated(view_function):
  def wrapped_view(request,*args, **kwargs):
    if not request.user.is_authenticated:
      return redirect('login')
    return view_function(request,*args, **kwargs)
  return wrapped_view

def check_not_authenticated(view_function):
  def wrapped_view(request,*args, **kwargs):
    if request.user.is_authenticated:
      return redirect('dashboard')
    return view_function(request,*args, **kwargs)
  return wrapped_view