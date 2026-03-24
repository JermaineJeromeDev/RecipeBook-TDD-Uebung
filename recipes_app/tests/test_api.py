from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from recipes_app.models import Recipe


class RecipeAPITestCase(APITestCase):
    def test_get_recipes_list(self):
        """Aufgabe 2: GET /api/recipes-list/ liefert 200 OK"""
        url = reverse('recipes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_recipe_create(self):
        """Aufgabe 3: POST /api/recipes-list/ erstellt ein Rezept"""
        user = User.objects.create(username='testuser', password='password123')

        url = reverse('recipes-list')
        data = {
            "title": "Mein Testrezept",
            "description": "Sehr lecker",
            "author": user.id 
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)