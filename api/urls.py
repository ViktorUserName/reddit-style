from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ThemeViewSet, CommentViewSet, VoteViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'themes', ThemeViewSet, basename='themes')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/vote/', VoteViewSet.as_view({'post': 'create', 'delete': 'destroy'}), name='post-vote'),
]