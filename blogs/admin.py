from django.contrib import admin

from .models import User,Blog,Post

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Post)

