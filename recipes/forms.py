from django import forms
from .models import Recipe, Ingredient, RecipeIngredient, Tag, Category

class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    status = forms.ChoiceField(choices=Recipe.STATUS_CHOICES, required=True)
    
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'category', 'description', 'instructions', 'image', 'status']

class RecipeIngredientForm(forms.ModelForm):
    custom_ingredient = forms.CharField(max_length=100, required=False, label='Custom Ingredient')
    
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit', 'is_optional']
    
    def clean(self):
        cleaned_data = super().clean()
        ingredient = cleaned_data.get('ingredient')
        custom_ingredient = cleaned_data.get('custom_ingredient')

        # If a custom ingredient is entered, make sure the user hasn't selected an existing ingredient
        if not ingredient and custom_ingredient:
            cleaned_data['ingredient'] = Ingredient.objects.create(name=custom_ingredient)  # Create new ingredient
        elif ingredient and custom_ingredient:
            raise forms.ValidationError("You can either select an existing ingredient or add a custom ingredient, not both.")

        return cleaned_data

class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ['name']