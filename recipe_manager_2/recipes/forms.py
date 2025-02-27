from django import forms
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'prep_time', 'category', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe name'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List ingredients'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Step-by-step instructions'}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in minutes'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comma-separated tags'}),
        }

class RecipeSearchForm(forms.Form):
    query = forms.CharField(
        required=False, 
        label="Search Recipes", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name or ingredient'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=False, 
        empty_label="All Categories", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
