"""Тесты представлений"""

import unittest
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from ..models import Album, Photo


class TestAlbumApi(unittest.TestCase):
    """Тест представлений Album и AlbumDetail"""

    token = Token.objects.get(user__username='admin')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_Album_list(self):
        """Тест списка альбомов"""
        response = self.client.get(reverse('album-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Album_detail(self):
        """Тест страницы альбома"""
        objs = Album.objects.all()
        if objs:
            response = self.client.get(reverse('album-detail', args=[objs[0].id]))
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPhotoApi(unittest.TestCase):
    """Тест представлений Photo и PhotoDetail"""

    token = Token.objects.get(user__username='admin')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_Photo_list(self):
        """Тест списка фото"""
        response = self.client.get(reverse('photo-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Photo_detail(self):
        """Тест страницы фото"""
        objs = Photo.objects.all()
        if objs:
            response = self.client.get(reverse('photo-detail', args=[objs[0].id]))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
