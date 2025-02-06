"""Bookmark View Functions"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def category(request):
    """Bookmark categories"""
    return render(request, 'bookmark/categories.html')
