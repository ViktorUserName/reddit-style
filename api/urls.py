from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ThemeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'themes', ThemeViewSet, basename='themes')

urlpatterns = [
    path('', include(router.urls)),
]