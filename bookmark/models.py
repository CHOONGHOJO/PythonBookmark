from django.db import models
from django.urls import reverse

# Create your models here.
# 모델 : 데이타베이스를 SQL없이 다루려고 사용
# 데이타를 객체화해서 다룬다.
# 모델 = 테이블
# 모델의 필드 = 데이타의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드컬럼 데이타값
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. d/b 의 column 종류
    # 2. 제약 사항 (몇글자까지)
    # 3. Form의 종류
    # 4. Form에서 제약 사항
    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
# model을 만들었다 => d/b에 어떤 data들을 어떤 형태로 넣을지 결정.
# migration => d/b에 model의 내용을 반영(tabel생성)
# makemigrations => model의 변경사항을 추적해서 기록