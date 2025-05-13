from rest_framework import serializers

from api.models import Theme, Post, Comment, Like



class PostReadSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    theme_name = serializers.CharField(source='theme.name', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'author_name', 'theme_name')
        # fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'theme')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class ThemeSerializer(serializers.ModelSerializer):
    posts = PostReadSerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = ('name', 'posts')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'