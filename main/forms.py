from django import forms
from django.utils.html import strip_tags
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'thumbnail', 'category', 'is_featured']

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        return strip_tags(description)
