"""Bookmark models"""
from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    """Categories Model"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta():
        """Meta"""
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    """Bookmark Model"""
    categories = models.ForeignKey(Category, related_name='bookmarks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
