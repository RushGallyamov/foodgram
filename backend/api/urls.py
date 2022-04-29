from api.views import IngredientsViewSet, RecipeViewSet, TagsViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('tags', TagsViewSet)
router.register('ingredients', IngredientsViewSet)
router.register('recipes', RecipeViewSet)

urlpatterns = [
    # path(
    #     'recipes/download_shopping_cart/',
    #     download_shopping_cart,
    #     name='download_shopping_cart'
    # ),
    path('', include(router.urls)),
]
