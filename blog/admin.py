# Register your models here.
from django.contrib import admin
from .models import Post  # Post 모델을 가져옵니다.

# Admin에 Post 모델을 등록합니다.
admin.site.register(Post)