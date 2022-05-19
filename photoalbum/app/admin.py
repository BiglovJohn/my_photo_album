"""Здесь происходит регистрация моделей в админ панели"""

from django.contrib import admin
from .models import Photo, Album


class PhotosAdmin(admin.ModelAdmin):
    """Класс для регистрации и настройки модели фотографии в админ панели"""
    list_display = ['user', 'created_at', 'photo']
    list_filter = ['user', 'created_at']
    readonly_fields = ['created_at']


class AlbumsAdmin(admin.ModelAdmin):
    """Класс для регистрации и настройки модели альбом в админ панели"""
    list_display = ['album_title', 'created_at', 'photo_count']
    list_filter = ['album_title', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Photo, PhotosAdmin)
admin.site.register(Album, AlbumsAdmin)
