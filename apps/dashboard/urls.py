from django.urls import path
from apps.bookmark.views import category
from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('categories/', category, name='category'),
]
