from django.contrib import admin

# Register your models here.
# 내가 만든 model을 관리자 page에서 관리할 수 있도록 등록
from .models import Bookmark

admin.site.register(Bookmark)