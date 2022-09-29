from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to = 'instagram/post/%Y/%m/%d') # 파일 이 안쌓이도록 도와줌 upload ~
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # model 안에 있는 객체들의 이름을 post object 에서 해당 이름으로 변환 기능
        #return f"custom post object({self.id})"
        #return "custom post object({}).format(self.id)"
        return self.message 
    