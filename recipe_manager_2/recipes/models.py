from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link recipes to users
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text="Time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
