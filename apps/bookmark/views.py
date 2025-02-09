"""Bookmark View Functions"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Category, Bookmark
from .forms import CategoryForm, BookmarkForm

@login_required
def categories(request):
    """Bookmark categories"""
    categories = request.user.categories.all()

    context = {
        "categories": categories
    }
    return render(request, 'bookmark/categories.html', context)

@login_required
def category(request, category_id):
    """Category detail"""
    category = Category.objects.get(pk=category_id)

    context = {
        "category": category
    }

    return render(request, 'bookmark/category.html', context)


@login_required
def category_add(request):
    """Adding a category"""
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()

            return redirect('categories')
    else:
        form = CategoryForm()

    context = {
        "form": form
    }

    return render(request, 'bookmark/category_add.html', context)

@login_required
def bookmark_add(request, category_id):
    """Adding a bookmark"""
    if request.method == "POST":
        form = BookmarkForm(request.POST)

        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.created_by = request.user
            bookmark.categories = Category.objects.get(id=category_id)
            bookmark.save()

            return redirect('category', category_id=category_id)
    else:
        form = BookmarkForm()

    context = {
        "form": form
    }

    return render(request, 'bookmark/bookmark_add.html', context)
