from django.forms import ModelForm

from .models import Category

class CategoryForm(ModelForm):
    """Adding category form"""
    class Meta:
        """Meta"""
        model = Category
        fields = ["title", "description"]
