from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class RecipeAPITestCase(APITestCase):
    def test_get_recipes_list(self):
        """Testet, ob die Liste der Rezepte erreichbar ist."""
        # Wir nutzen 'recipes-list' als Namen für unsere URL später
        url = "/recipes-list"
        response = self.client.get(url)

        # Dieser Test wird fehlschlagen (404), da die URL noch nicht existiert
        self.assertEqual(response.status_code, status.HTTP_200_OK)