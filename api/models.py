from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    vote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'comment by {self.author.username}: {self.content[:30]}'

class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_likes')


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_like')
        ]

    def __str__(self):
        return f'{self.user.username} поставил нравится {self.post.title} !!!'