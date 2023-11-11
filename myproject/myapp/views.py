from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('myapp:dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'myapp/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('myapp:dashboard')
        else:
            messages.error(request, 'Invalid login credentials.')

    else:
        form = AuthenticationForm()

    return render(request, 'myapp/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('myapp:login') 