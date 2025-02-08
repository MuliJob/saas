from django.urls import path
from apps.bookmark.views import categories, category, category_add
from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('categories/', categories, name='categories'),
  path('categories/<int:category_id>/', category, name='category'),
  path('add-category/', category_add, name='category_add'),
]
