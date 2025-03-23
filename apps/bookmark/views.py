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
def category_edit(request, category_id):
    """Editing a category"""
    category = Category.objects.filter(created_by=request.user).get(pk=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    context = {
        "form": form,
        "category": category,
    }

    return render(request, 'bookmark/category_edit.html', context)


@login_required
def category_delete(request, category_id):
    """Deleting a category"""
    category = Category.objects.filter(created_by=request.user).get(pk=category_id)
    category.delete()

    return redirect('categories')

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


@login_required
def bookmark_edit(request, category_id, bookmark_id):
    """Editing a bookmark"""
    bookmark = Bookmark.objects.filter(created_by=request.user).get(pk=bookmark_id)

    if request.method == "POST":
        form = BookmarkForm(request.POST, instance=bookmark)

        if form.is_valid():
            form.save()

            return redirect('category', category_id=category_id)
    else:
        form = BookmarkForm(instance=bookmark)

    context = {
        "form": form,
        "bookmark": bookmark,
    }

    return render(request, 'bookmark/bookmark_edit.html', context)


@login_required
def bookmark_delete(request, category_id, bookmark_id):
    """Deleting a bookmark"""
    bookmark = Bookmark.objects.filter(created_by=request.user).get(pk=bookmark_id)
    bookmark.delete()

    return redirect('category', category_id=category_id)
