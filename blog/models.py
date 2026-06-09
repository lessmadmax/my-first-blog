from django.db import models
from django.utils import timezone
# 1. settings를 사용하기 위해 임포트 추가
from django.conf import settings 

class Post(models.Model):
    # 2. 'author =' 라는 변수명을 명시해 주어야 합니다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='intruder_image/%Y/%m/%d/', default='intruder_image/default_error.png')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title