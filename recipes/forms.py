from django import forms
from .models import Recipe, RecipeIngredient, Tag, Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'category', 'description', 'instructions', 'image', 'status']
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    status = forms.ChoiceField(choices=Recipe.STATUS)

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit', 'is_optional']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']