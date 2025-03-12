from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-created_at')
    template_name = "recipes/index.html"
    paginate_by = 6

# View to create a recipe (only for logged-in users)
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_create.html'
    fields = ['title', 'slug', 'category', 'description', 'instructions', 'image', 'status']
    
    # Automatically assign the user to the recipe
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # Redirect to the recipe detail page after successful creation
    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'slug': self.object.slug})

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

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    ingredients = recipe.ingredients.all() 

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe,
         "ingredients": ingredients},
    )
    
# View to list all recipes
class UserRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'
    queryset = Recipe.objects.all().order_by('-created_at')
    
    def get_queryset(self):
        # Only fetch recipes for the logged-in user
        return Recipe.objects.filter(user=self.request.user)
    
# Recipe Edit View (Only for the recipe owner)
class RecipeEditView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_edit.html'
    fields = ['title', 'slug', 'category', 'description', 'instructions', 'image', 'status']
    
    # Check if the logged-in user is the owner of the recipe
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            # Redirect to the recipe's detail page if the user is not the owner
            return redirect('recipe_detail', slug=obj.slug)
        return obj
    
    # Redirect to the recipe detail page after successful update
    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'slug': self.object.slug})