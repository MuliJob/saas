"""Core Views"""
from django.shortcuts import render

def homepage(request):
    """Home page"""
    return render(request, 'core/base.html')
