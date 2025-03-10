from django import forms
from .models import Recipe, Ingredient, Tag

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'category', 'ingredients', 'tags']
        
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(), required=False)