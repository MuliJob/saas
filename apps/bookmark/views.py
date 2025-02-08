"""Bookmark View Functions"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Category
from .forms import CategoryForm

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
