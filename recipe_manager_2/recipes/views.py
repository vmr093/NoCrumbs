from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Recipe, Favorite, Category
from .forms import RecipeForm, RecipeSearchForm

# 📄 Recipe List with Search, Category Filter, & Pagination
def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()  # Fetch all categories for the second navbar
    search_form = RecipeSearchForm(request.GET)

    # Apply search and filter logic
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        category = request.GET.get('category')  # Get category from URL parameter

        if query:
            recipes = recipes.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))

        if category and category != "All":
            recipes = recipes.filter(category=category)

    # Paginate results (6 recipes per page)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)

    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'search_form': search_form,
        'categories': categories
    })

# 📌 Recipe Detail Page
@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    is_favorited = Favorite.objects.filter(user=request.user, recipe=recipe).exists()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'is_favorited': is_favorited})

# ➕ Add New Recipe
@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/recipe_form.html', {'form': form})

# ✏️ Edit Recipe
@login_required
def recipe_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/recipe_form.html', {'form': form})

# 🗑 Delete Recipe
@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

# ⭐ Favorite Recipe (Toggle)
@login_required
def favorite_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:  # If already favorited, remove it
        favorite.delete()

    return redirect(request.META.get('HTTP_REFERER', 'recipe_list'))  # Redirects back to the previous page

# ❤️ Favorite Recipes List
@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('recipe')
    return render(request, 'recipes/favorites.html', {'favorites': favorites})

# 📄 List Recipes by Category
def recipes_by_category(request, category_name):
    categories = Category.objects.all()
    recipes = Recipe.objects.filter(category=category_name)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    recipes = paginator.get_page(page_number)

    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'categories': categories,
        'selected_category': category_name
    })
