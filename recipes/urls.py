from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/', views.UserRecipeListView.as_view(), name='recipe_list'),
]
