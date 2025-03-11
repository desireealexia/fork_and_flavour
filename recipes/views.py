from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DetailView, ListView
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
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'
    
# View to list all recipes
class UserRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'
    queryset = Recipe.objects.all().order_by('-created_at')
    
    def get_queryset(self):
        # Only fetch recipes for the logged-in user
        return Recipe.objects.filter(user=self.request.user)