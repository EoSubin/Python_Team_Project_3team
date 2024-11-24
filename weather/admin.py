from django.contrib import admin
from .models import Outfit  # Outfit 모델을 가져옵니다.

# Outfit 모델을 관리자 페이지에 등록합니다.
admin.site.register(Outfit)
