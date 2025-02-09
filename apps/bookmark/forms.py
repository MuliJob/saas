"""Forms"""
from django.forms import ModelForm

from .models import Bookmark, Category

class CategoryForm(ModelForm):
    """Adding category form"""
    class Meta:
        """Meta"""
        model = Category
        fields = ["title", "description"]

class BookmarkForm(ModelForm):
    """Adding category form"""
    class Meta:
        """Meta"""
        model = Bookmark
        fields = ["title", "description", 'url']
