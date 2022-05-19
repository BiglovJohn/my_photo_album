""" В данном фале происходит создание и настройка форм """

from django import forms
from .models import Photo, Album


class PhotosForm(forms.ModelForm):
    """ Форма модели фото """

    class Meta:
        """ Определение параметров в мета классе фото """

        model = Photo
        fields = '__all__'


class AlbumsForm(forms.ModelForm):
    """ Форма модели альбом """

    class Meta:
        """ Определение параметров в мета классе альбом """

        model = Album
        fields = '__all__'
