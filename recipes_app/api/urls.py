from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
# Wichtig: 'recipes-list' als Pfad, damit reverse('recipes-list') funktioniert
router.register(r'recipes-list', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
]

