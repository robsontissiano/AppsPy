from django.db import models

class Recipe(models.Model):
    pub_date = models.DateTimeField('Date Published', auto_now_add = True)
    title = models.CharField(max_length=200)
    instructions = models.TextField()

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients")
    ingredient = models.CharField(max_length=255)