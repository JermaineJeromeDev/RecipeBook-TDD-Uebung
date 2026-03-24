from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class RecipeAPITestCase(APITestCase):
    def test_get_recipes_list(self):
        """Aufgabe 2: GET /api/recipes-list/ liefert 200 OK"""
        url = reverse('recipes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)