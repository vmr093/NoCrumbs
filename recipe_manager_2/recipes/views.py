from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Recipe
from .forms import RecipeForm, UserRegistrationForm

# ✅ User Authentication Views

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encrypt password
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('recipe_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'recipes/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('recipe_list')


# ✅ Recipe CRUD Views (Login Required)

@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user)  # Show only user's recipes
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user  # Assign the recipe to the logged-in user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)  # Ensure user owns the recipe
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)  # Restrict access
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)  # Restrict access
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})
