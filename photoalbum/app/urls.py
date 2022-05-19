"""Файл для регистрации представлений и назначения эндпоинтов"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PhotoList, AlbumList, AlbumDetail, PhotoDetail

urlpatterns = [
    path('api/v1/photo/', PhotoList.as_view(), name='photo-list'),
    path('api/v1/photo/<int:pk>/', PhotoDetail.as_view(), name='photo-detail'),
    path('api/v1/album/', AlbumList.as_view(), name='album-list'),
    path('api/v1/album/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
