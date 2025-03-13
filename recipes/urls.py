from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<slug:slug>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('profile/', views.profile, name='profile'),
    path('recipes/', views.UserRecipeListView.as_view(), name='recipe_list'),
]
