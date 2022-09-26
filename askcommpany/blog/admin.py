from django.contrib import admin
from.models import Post # model 에 있는 Post class 를 불러옴 안해주면 Post 데이터베이스를 인식을 못함
# Register your models here.

admin.site.register(Post)
