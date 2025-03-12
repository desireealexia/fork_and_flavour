from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe/create/', views.create_recipe, name='recipe_create'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/', views.UserRecipeListView.as_view(), name='recipe_list'),
    path('recipe/<slug:slug>/edit/', views.RecipeEditView.as_view(), name='recipe_edit'),
]
