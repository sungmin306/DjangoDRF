from django.contrib import admin
from . models import Post

from django.utils.safestring import mark_safe
# Register your models here.
# admin.site.register(Post)

#2번째 방법
# class PostAdmin(admin,ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)'

#3번째 방법
@admin.register(Post)# 장식자문법 -> Wrapping(감싸는 역할)
class PostAdmin(admin.ModelAdmin):
    #html 없이 admin 페이지 커스텀 칼럼 수정
    list_display = ['id','photo_tag','message','created_at','is_public','updated_at'] # id= pk(primary key)
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            #post.photo.url
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

    def message_mengh(self,post):
        return f"{len(post.message)}글자"