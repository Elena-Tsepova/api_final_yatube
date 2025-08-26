from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Comment, Follow

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
