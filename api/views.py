from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Post, Theme, Comment, Vote
from api.serializers import ThemeSerializer, PostReadSerializer, PostCreateSerializer, CommentSerializer, VoteSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return super().get_serializer_class()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class VoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VoteSerializer

    def create(self, request, post_id=None):
        serializer = self.serializer_class(data=request.data, context={'request': request, 'view': self})
        serializer.is_valid(raise_exception=True)
        vote = serializer.save()
        return Response(self.serializer_class(vote).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, post_id=None):
        user = request.user
        deleted, _ = Vote.objects.filter(user=user, post_id=post_id).delete()
        if deleted:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Голос не найден.'}, status=status.HTTP_404_NOT_FOUND)