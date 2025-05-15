from rest_framework import serializers

from api.models import Theme, Post, Comment, Vote


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.PrimaryKeyRelatedField(source='post', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'parent', 'post_id')

class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'parent', 'post')


class PostReadSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    theme_name = serializers.CharField(source='theme.name', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ('id','title', 'content', 'author_name', 'theme_name', 'vote_count', 'comments')
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


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['type']

    def validate(self, attrs):
        user = self.context['request'].user
        post_id = self.context['view'].kwargs.get('post_id')

        # Проверим, если уже есть голос, но если хотим обновлять - пропускаем в create
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        post_id = self.context['view'].kwargs.get('post_id')

        vote_type = validated_data['type']

        vote, created = Vote.objects.update_or_create(
            user=user,
            post_id=post_id,
            defaults={'type': vote_type}
        )
        return vote