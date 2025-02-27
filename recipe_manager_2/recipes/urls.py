from django.urls import path
from . import views

urlpatterns = [
    # ✅ Recipe CRUD URLs
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:recipe_id>/edit/', views.recipe_update, name='recipe_update'),
    path('recipe/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),

    # ✅ User Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

