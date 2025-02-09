"""Dashboard views"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from apps.bookmark.models import Bookmark

@login_required
def dashboard(request):
    """Dashboard"""
    bookmarks = request.user.bookmarks.all()[0:5]

    context = {
        "bookmarks": bookmarks
    }
    return render(request, 'dashboard/dashboard.html', context)
