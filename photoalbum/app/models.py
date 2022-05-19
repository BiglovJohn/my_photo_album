"""Файл для инициализации моделяей приложения 'app'"""
import os

from PIL import Image
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

_MAX_SIZE = 150


def user_directory_path(instance, filename):
    """Путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>"""
    return f'user_{instance.user}/{filename}'


def max_value(image_file):
    """Валидатор для ограничения размера загружаемой картинки"""
    if image_file.size >= 5 * 1024 * 1024:
        raise ValueError('Максимальный размер файла 5 Мб')


class Album(models.Model):
    """Класс для описания модели альбом"""
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь'
                             )
    album_title = models.CharField(max_length=30,
                                   verbose_name='Название альбома'
                                   )
    created_at = models.DateTimeField(default=timezone.now,
                                      auto_created=timezone.now,
                                      verbose_name='Дата создания'
                                      )
    photo_count = models.IntegerField(default=0, verbose_name='Количество фотографий')

    def __str__(self):
        return str(self.album_title)

    class Meta:
        """Определение параметров в мета классе альбом"""
        db_table = 'db.album'
        ordering = ['created_at']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Photo(models.Model):
    """Класс для описания модели фото"""
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             )
    album = models.ForeignKey(to=Album,
                              on_delete=models.CASCADE,
                              verbose_name='Идентификатор альбома'
                              )
    title = models.CharField(max_length=50, default='', verbose_name='Название')
    photo = models.ImageField(upload_to=user_directory_path,
                              validators=[max_value, FileExtensionValidator([
                                  'jpg',
                                  'jpeg',
                                  'png'],
                                  'Поддерживаются файлы JPG, JPEG и PNG')
                                          ],
                              verbose_name='Фотография')
    created_at = models.DateTimeField(default=timezone.now,
                                      auto_created=timezone.now,
                                      verbose_name='Дата публикации'
                                      )

    class Meta:
        """Определение параметров в мета классе фото"""
        db_table = 'db.photo'
        ordering = ['created_at']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
