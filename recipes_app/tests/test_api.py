from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from recipes_app.models import Recipe


class RecipeAPITestCaseHappy(APITestCase):
    """Hier testen wir alles, was funktionieren SOLL (mit Auth)."""
    def setUp(self):
        self.user = User.objects.create_user(username='happyuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Wir erstellen vorab ein Rezept für die Detail-Tests
        self.recipe = Recipe.objects.create(
            title="Testsuppe", 
            description="Lecker", 
            author=self.user
        )

    def test_post_recipe_authenticated(self):
        """Aufgabe 5: Eingeloggter User erstellt Rezept."""
        url = reverse('recipes-list')
        data = {
            "title": "Auth Rezept",
            "description": "Mit Token erstellt",
            "author": self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_recipe_detail_authenticated(self):
        """Aufgabe 6: Rezept-Detail abrufen mit Auth (200 OK)"""
        # Hier nutzen wir kwargs für die ID des Rezepts
        url = reverse('recipes-detail', kwargs={'pk': self.recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Testsuppe")


class RecipeAPITestCaseUnhappy(APITestCase):
    """Hier testen wir Fehlerfälle (ohne Auth)."""
    def setUp(self):
        self.user = User.objects.create_user(username='otheruser')
        self.recipe = Recipe.objects.create(
            title="Geheimrezept", 
            description="Nicht gucken", 
            author=self.user
        )

    def test_post_recipe_unauthorized(self):
        """Aufgabe 4: POST ohne Auth muss scheitern."""
        url = reverse('recipes-list')
        data = {"title": "Illegal", "description": "Kein Token", "author": 1}
        response = self.client.post(url, data, format='json')

        # Da wir oben IsAuthenticatedOrReadOnly gesetzt haben, 
        # wird hier ein 401 (Unauthorized) erwartet.
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_recipe_detail_unauthorized(self):
        """Aufgabe 8: Detailabruf ohne Auth gibt 401 (nach Aufgabe 7)"""
        url = reverse('recipes-detail', kwargs={'pk': self.recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)