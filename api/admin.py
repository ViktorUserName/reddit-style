from django.contrib import admin

from api.models import Theme, User, Comment, Post, Vote

admin.site.register(Theme)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vote)