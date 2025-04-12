from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Category, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'category', 'status', 'created_at')
    inlines = [RecipeIngredientInline]
    search_fields = ['title', 'category']
    list_filter = ('status', 'created_at',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'instructions',)


# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredient)
