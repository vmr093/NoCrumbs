from django.urls import path
from .views import (
    recipe_list, recipe_create, recipe_detail, recipe_update, recipe_delete,
    favorite_recipe, favorite_list
)

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('recipe/new/', recipe_create, name='recipe_create'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/edit/', recipe_update, name='recipe_update'),
    path('recipe/<int:recipe_id>/delete/', recipe_delete, name='recipe_delete'),
    path('recipe/<int:recipe_id>/favorite/', favorite_recipe, name='favorite_recipe'),
    path('favorites/', favorite_list, name='favorite_list'),
]

