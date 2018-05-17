from django.db import models

# Create your models here.

# ORM

class Bookmark(models.Model):
    # Field / Column 명세
    # FieldName = Field 자료형
    # 필드 종류의 목적 : 1. 데이터베이스에 어떤식으로 데이터 저장 ?
    # 2. 사용자의 입력을 받을때 어떤 form태그를 보여줄것인가 ?
    # 2 - 1. 입력 폼의 제한사항 설정, 유효성 검사 생성
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')


    # Inner Class
    # 모델을 다룰시 옵션값.
    class Meta:
        # 정렬 방식
        # - : 내림차순
        # + (혹은 생략) : 오름차순
        ordering = ['site_name']

    def __str__(self):
        return self.site_name

    # 인서트 완료시 이동할 주소 지정
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bookmark:detail', args=[str(self.id)])




