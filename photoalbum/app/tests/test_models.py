"""Тесты моделей"""

from djoser.conf import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from ..models import Album, Photo


class PhotoTestCase(APITestCase):
    """Класс тестов методов API"""
    token = Token.objects.get(user__username='admin')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    content = Photo.objects.create(title='test_photo', user_id=4, album_id=17)

    def test_DELETE_content(self):
        """Тест метода DELETE"""
        user = User.objects.create(email='person@example.com', username='Test user')
        self.client.force_authenticate(user=user)
        url = reverse('photo-detail', kwargs={'pk': self.content.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AlbumTestCase(APITestCase):
    """Класс тестов методов API"""
    token = Token.objects.get(user__username='admin')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    content = Album.objects.create(album_title='test_album', user_id=4)

    def test_DELETE_content(self):
        """Тест метода DELETE"""
        user = User.objects.create(email='person@example.com', username='Test user')
        self.client.force_authenticate(user=user)
        url = reverse('album-detail', kwargs={'pk': self.content.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
