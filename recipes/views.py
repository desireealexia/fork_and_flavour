from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import Http404

from . import models

# Create your views here.
# View to list all recipes on index.html
class RecipeListView(generic.ListView):
    model = models.Recipe
    template_name = "recipes/index.html"
    queryset = models.Recipe.objects.filter(status=1).order_by('-created_at')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()  # Pass all categories to the template
        return context
    
    def get_queryset(self):
        category_filter = self.request.GET.get('category')
        if category_filter:
            return self.queryset.filter(category__id=category_filter)  # Using 'id' field for filtering
        return self.queryset
    
def recipe_search(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    
    # Filter recipes based on the search query
    recipes = models.Recipe.objects.filter(
        Q(title__icontains=query) | Q(ingredients__ingredient__name__icontains=query)
    ).distinct()

    if category_id:
        recipes = recipes.filter(category_id=category_id)

    # Fetch categories without counting recipes
    categories = models.Category.objects.all().order_by('id')

    # Pagination logic
    paginator = Paginator(recipes, 6)  # 6 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/recipe_search.html', {
        'recipes': page_obj,
        'query': query,
        'categories': categories,
        'category_id': category_id,
    })

# View to display the details of a single recipe
def recipe_detail(request, slug):
    """
    Display an individual :model:`recipes.Recipe`.

    **Context**

    ``post``
        An instance of :model:`recipes.Recipe`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    recipe = get_object_or_404(models.Recipe, slug=slug)
    ingredients = recipe.ingredients.all() 
    
    if recipe.status == 0 and recipe.user != request.user:
        return redirect('profile')
    
    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe,
         "ingredients": ingredients},
    )

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'category', 'description', 'instructions', 'image', 'status']
    
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.slug = slugify(self.object.title)
        
        instructions_text = form.cleaned_data['instructions'].strip()
        instructions_list = instructions_text.split('\n')
        formatted_instructions = ''.join(f'<li>{step.strip()}</li>' for step in instructions_list if step.strip())
        self.object.instructions = f"<ol>{formatted_instructions}</ol>"
    
        self.object = form.save()

        # Extract ingredient data from POST request
        ingredient_names = self.request.POST.getlist('ingredient_name[]')
        ingredient_quantities = self.request.POST.getlist('ingredient_quantity[]')
        ingredient_units = self.request.POST.getlist('ingredient_unit[]')
        ingredient_optionals = self.request.POST.getlist('ingredient_optional[]')

        for i in range(len(ingredient_names)):
            name = ingredient_names[i].strip()
            quantity = ingredient_quantities[i].strip() or None
            unit = ingredient_units[i].strip() or ''
            is_optional = 'true' in ingredient_optionals[i:i+1]

            # Create or get the ingredient
            ingredient, created = models.Ingredient.objects.get_or_create(name=name)

            # Create RecipeIngredient entry
            models.RecipeIngredient.objects.create(
                recipe=self.object,
                ingredient=ingredient,
                quantity=quantity,
                unit=unit,
                is_optional=is_optional
            )
            
        messages.success(self.request, 'Recipe created successfully!')
        return redirect(self.success_url)
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'category', 'description', 'instructions', 'image', 'status']
    
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.user

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.slug = slugify(self.object.title)
        
        instructions_text = form.cleaned_data['instructions'].strip()
        instructions_list = instructions_text.split('\n')
        formatted_instructions = ''.join(f'<li>{step.strip()}</li>' for step in instructions_list if step.strip())
        self.object.instructions = f"<ol>{formatted_instructions}</ol>"
    
        self.object = form.save()
        
        # Clear old ingredients
        models.RecipeIngredient.objects.filter(recipe=self.object).delete()

        # Extract and save new ingredient data
        ingredient_names = self.request.POST.getlist('ingredient_name[]')
        ingredient_quantities = self.request.POST.getlist('ingredient_quantity[]')
        ingredient_units = self.request.POST.getlist('ingredient_unit[]')
        ingredient_optionals = self.request.POST.getlist('ingredient_optional[]')

        for i in range(len(ingredient_names)):
            name = ingredient_names[i].strip()
            quantity = ingredient_quantities[i].strip() or None
            unit = ingredient_units[i].strip() or ''
            is_optional = 'true' in ingredient_optionals[i:i+1]

            ingredient, created = models.Ingredient.objects.get_or_create(name=name)
            models.RecipeIngredient.objects.create(
                recipe=self.object,
                ingredient=ingredient,
                quantity=quantity,
                unit=unit,
                is_optional=is_optional
            )
        
        messages.success(self.request, 'Recipe updated successfully!')
        return redirect(self.success_url)  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        recipe_ingredients = models.RecipeIngredient.objects.filter(recipe=recipe)
        raw_instructions = recipe.instructions.replace("<ol>", "").replace("</ol>", "").replace("<li>", "").replace("</li>", "\n").strip()
        
        context['recipe_ingredients'] = recipe_ingredients
        context['raw_instructions'] = raw_instructions
        return context

    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipe_list')
    
    def test_func(self):
        recipe = self.get_object()
        messages.success(self.request, 'Recipe deleted successfully!')
        return self.request.user == recipe.user  

# View to list all recipes for a specific user
class UserRecipeListView(LoginRequiredMixin, ListView):
    model = models.Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'
    queryset = models.Recipe.objects.all().order_by('-created_at')
    
    def get_queryset(self):
        # Only fetch recipes for the logged-in user
        return models.Recipe.objects.filter(user=self.request.user)
