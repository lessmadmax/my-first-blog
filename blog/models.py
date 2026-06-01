from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 작성자: Django의 기본 User 모델과 연결 (옵션)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    # 제목: 최대 200자 제한의 문자열
    title = models.CharField(max_length=200)
    
    # 본문: 글자 수 제한이 없는 긴 텍스트
    text = models.TextField()
    
    # 생성일: 기본값으로 현재 시간이 저장됨
    created_date = models.DateTimeField(default=timezone.now)
    
    # 게시일: views.py에서 사용되는 핵심 필드 (비어있을 수 있음)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """게시 버튼을 누르면 현재 시간으로 게시일을 저장하는 메서드"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """관리자 페이지나 쉘에서 제목이 보이도록 설정"""
        return self.title