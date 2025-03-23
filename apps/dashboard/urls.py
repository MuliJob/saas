from django.urls import path
from apps.bookmark.views import categories, category, category_add, bookmark_add, bookmark_edit, category_edit, category_delete
from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('categories/', categories, name='categories'),
  path('categories/<int:category_id>/', category, name='category'),
  path('add-category/', category_add, name='category_add'),
  path('categories/<int:category_id>/edit/', category_edit, name='category_edit'),
  path('categories/<int:category_id>/delete/', category_delete, name='category_delete'),
  path('categories/<int:category_id>/add-bookmark/', bookmark_add, name='bookmark_add'),
  path('categories/<int:category_id>/edit-bookmark/<int:bookmark_id>/',
  bookmark_edit, name='bookmark_edit'),
]
