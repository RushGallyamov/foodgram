from djoser.serializers import UserCreateSerializer
from recipes.models import Ingredient, Recipe, Tag, IngredientForRecipe
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.shortcuts import get_list_or_404


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        )


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'color',
            'slug'
        ]


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'measurement_unit'
        ]


class IngredientForRecipeSerializer(ModelSerializer):
    class Meta:
        model = IngredientForRecipe
        fields = [
            'id',
            'name',
            'measurement_unit',
            'recipe'
        ]


class RecipeSerializer(ModelSerializer):
    author = UserSerializer(
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)

    def create(self, validated_data):
        if validated_data['tags']:
            kwargs = validated_data.pop('tags')
            tags = Tag.objects.get_list_or_404(Tag, **kwargs)
            return Recipe.objects.create(tags=tags, data=validated_data)


    class Meta:
        model = Recipe
        fields = [
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time'
        ]
