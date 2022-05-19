""" Файл для настройки приложений """

from django.apps import AppConfig


class MyAppConfig(AppConfig):
    """ Настройка типа поля для приложения 'app' """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
