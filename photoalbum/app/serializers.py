"""Файл c сериализаторами"""

from rest_framework import serializers
from django.utils import timezone

from .models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    """Сериализатор модели фото"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(default=timezone.now, read_only=True)

    class Meta:
        """Определение параметров в мета классе фото"""
        model = Photo
        read_only_fields = ['created_at']
        fields = ['user', 'user_id', 'title', 'photo', 'created_at', 'album']


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбом"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.ReadOnlyField(default=timezone.now)
    photo_count = serializers.IntegerField(source='photo_set.count', read_only=True)

    class Meta:
        """Определение параметров в мета классе альбом"""
        model = Album
        read_only_fields = ['created_at']
        fields = ['user', 'user_id', 'album_title', 'created_at', 'photo_count']


class PhotoPutSerializer(serializers.ModelSerializer):
    """Сериализатор модели фото для обновления данных"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(default=timezone.now, read_only=True)

    class Meta:
        """Определение параметров в мета классе для обновления данных фото"""
        model = Photo
        read_only_fields = ['created_at', 'photo', 'album']
        fields = ['user', 'user_id', 'title', 'photo', 'created_at']


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбом для детального представления"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.ReadOnlyField(default=timezone.now)
    photos = PhotoSerializer(many=True, read_only=True, source='photo_set')

    class Meta:
        """Определение параметров в мета классе альбом для детального представления"""
        model = Album
        read_only_fields = ['created_at']
        fields = ['user', 'user_id', 'album_title', 'created_at', 'photos']
