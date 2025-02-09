from django.contrib import admin

from .models import Bookmark, Category

admin.site.register(Category)
admin.site.register(Bookmark)
