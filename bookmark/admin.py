from django.contrib import admin

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록
from .models import Bookmark

admin.site.register(Bookmark)
# admin.py 의 목적은 모델을 admin페이지에 등록해서 볼 수 있도록 하는데에 있다.
