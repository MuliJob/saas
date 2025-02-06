"""Core Views"""
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    """Home page"""
    return render(request, 'core/homepage.html')

def signup(request):
    """User Registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {"form": form})
