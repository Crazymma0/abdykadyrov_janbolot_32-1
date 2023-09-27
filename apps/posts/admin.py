from django.contrib import admin

from apps.posts.models import Post, Hashtag


admin.site.register(Post)
admin.site.register(Hashtag)
