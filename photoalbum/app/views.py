""" Файл с представлениями """
from django.http import Http404
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin,\
    RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.response import Response

from .models import Photo, Album
from .serializers import PhotoSerializer, AlbumSerializer, PhotoPutSerializer, AlbumDetailSerializer


class PhotoList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка фотографий и загрузки новой"""
    serializer_class = PhotoSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Photo.objects.filter(user=user)
        photo_name = self.request.query_params.get('name')
        if photo_name:
            queryset.filter(name=photo_name)
        return queryset

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['album']

    def get(self, request):
        """Определение метода GET"""
        return self.list(request)

    def post(self, request):
        """Определение метода POST"""
        return self.create(request)


class AlbumList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка альбомов и создания нового"""
    serializer_class = AlbumSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Album.objects.filter(user=user)
        album_name = self.request.query_params.get('album_title')
        if album_name:
            queryset.filter(album_title=album_name)
        return queryset

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'photo_count']

    def get(self, request):
        """Определение метода GET"""
        return self.list(request)

    def post(self, request):
        """Определение метода POST"""
        return self.create(request)


class PhotoDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                  GenericAPIView):
    """Представление для детальной информации о фотографии,
     а так же его редактирования и удаления"""
    serializer_class = PhotoPutSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Photo.objects.filter(user=user)
        album_name = self.request.query_params.get('name')
        if album_name:
            queryset.filter(name=album_name)
        return queryset

    def get(self, request, *args, **kwargs):
        """Определение метода GET"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Определение метода PUT"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Определение метода DELETE"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для детальной информации об альбоме, а так же его редактирования и удаления"""
    serializer_class = AlbumDetailSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Album.objects.filter(user=user)
        album_name = self.request.query_params.get('name')
        if album_name:
            queryset.filter(name=album_name)
        return queryset

    def get(self, request, *args, **kwargs):
        """Определение метода GET"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Определение метода PUT"""
        serializer = AlbumSerializer(partial=True)
        return self.update(request, *args, **kwargs), serializer

    def delete(self, request, *args, **kwargs):
        """Определение метода DELETE"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
