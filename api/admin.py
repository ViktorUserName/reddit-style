from django.contrib import admin

from api.models import Theme, User, Comment, Like, Post

admin.site.register(Theme)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)