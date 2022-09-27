from django.contrib import admin
from . models import Post
# Register your models here.
admin.site.register(Post)

#2번째 방법
# class PostAdmin(admin,ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)'

#3번째 방법
# @admin.regitser(Post) 장식자문법 -> Wrapping(감싸는 역할)
# class PostAdmin(admin.ModelAdmin):
#     pass