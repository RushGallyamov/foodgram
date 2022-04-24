from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from colorfield.fields import ColorField
from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    measurement_unit = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    # ingredients = models.ManyToManyField(Ingredient)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=255)
    cooking_time = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(600)
        ]
    )
    is_favorited = models.BooleanField(default=True)
    is_in_shopping_cart = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class IngredientForRecipe(Ingredient):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
    )
    amount = models.IntegerField(default=1)
