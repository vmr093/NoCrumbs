from django.db import models
from django.contrib.auth.models import User

# ✅ Predefined Categories for Recipes
CATEGORY_CHOICES = [
    ("Vegetarian", "Vegetarian"),
    ("Dinner", "Dinner"),
    ("Lunch", "Lunch"),
    ("Snack", "Snack"),
    ("Dessert", "Dessert"),
    ("Vegan", "Vegan"),
    ("Halal", "Halal"),
]

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name  # ✅ Ensures the correct category name is used in filtering


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text="Time in minutes")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)  # ✅ Uses predefined categories
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # ✅ Method to get category name
    def get_category_display_name(self):
        return dict(CATEGORY_CHOICES).get(self.category, "Uncategorized")


# ⭐ Favorite Model (Users can favorite recipes)
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # Prevents duplicate favorites

    def __str__(self):
        return f"{self.user.username} - {self.recipe.name}"
