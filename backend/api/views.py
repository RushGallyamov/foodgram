from django.conf import settings

from recipes.models import Ingredient, Recipe, Tag
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from users.models import User

from .serializers import (IngredientSerializer, RecipeSerializer,
                          TagSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_serializer_class(self):
        if self.action == "create":
            return settings.DJOSER.SERIALIZERS.user_create
        elif self.action == "me":
            return settings.DJOSER.SERIALIZERS.current_user
        return self.serializer_class

    def get_permission(self):
        if self.action == 'list':
            self.permission_classes = settings.PERMISSIONS.user_list


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
