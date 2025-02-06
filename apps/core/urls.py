"""Urls Pattern"""
from django.contrib import path
from . import views

urlpatterns = [
  path('', views.homepage, name='home')
]
