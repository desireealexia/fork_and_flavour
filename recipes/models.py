from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from fractions import Fraction

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    instructions = models.TextField()
    image = CloudinaryField('image', blank=True, null=True) 
    status = models.IntegerField(choices=STATUS, default=0)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.title
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    is_optional = models.BooleanField(default=False)

    def format_quantity(self):
        """Convert decimal quantities to fractions or remove decimals if possible."""
        if self.quantity is None:
            return ""
        
        try:
            fraction = Fraction(self.quantity).limit_denominator(8)
            if fraction.denominator == 1:
                return str(fraction.numerator) 
            return f"{fraction.numerator}/{fraction.denominator}" 
        except ValueError:
            return str(self.quantity) 
        
    def __str__(self):
        quantity_str = self.format_quantity()  # Format the quantity
        if quantity_str and self.unit:
            return f"{quantity_str} {self.unit} of {self.ingredient.name}"
        elif quantity_str:
            return f"{quantity_str} of {self.ingredient.name}"
        elif self.unit:
            return f"{self.unit} of {self.ingredient.name}"
        else:
            return f"{self.ingredient.name}"