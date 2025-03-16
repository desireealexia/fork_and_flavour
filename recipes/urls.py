from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('recipes/', views.UserRecipeListView.as_view(), name='recipe_list'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<slug:slug>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]
