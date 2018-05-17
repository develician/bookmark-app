from django.contrib import admin
from .models import Bookmark

# 작성한 모델을 관리자 페이지에서 다룰수있도록 등록
# 모델을 다루는데 관련된 옵션값을 설정
# Register your models here.

admin.site.register(Bookmark)