from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import *
from django.http import HttpResponse
from weather.models import Outfit  
import requests
from weather.views import get_weather_data
from .models import UserProfile, OOTD
from feedback.models import Feedback

# 회원가입 뷰
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 자동 로그인
            return redirect('dislike_survey')  # 회원가입 성공 후 이동할 URL
        else:
            print(form.errors)  # 에러 출력 (디버깅 용도)
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

# 로그인 뷰
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('weather:today_weather')  # 성공적으로 로그인한 후 이동할 URL
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# 로그아웃 뷰
def logout_view(request):
    logout(request)
    return redirect('users:login')  # 로그아웃 후 이동할 URL


def my_page_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Feedback 데이터를 가져옴 (로그인 사용자 기준)
    feedbacks = Feedback.objects.filter(user=request.user).order_by('-created_at')  # 최신순 정렬

    return render(request, 'users/my_page.html', {
        'user_profile': user_profile,
        'feedbacks': feedbacks,  # Feedback 데이터 전달
    })


def upload_ootd_view(request):
    if request.method == 'POST':
        condition = request.POST.get('condition')  # 사용자가 선택한 컨디션
        activity = request.POST.get('activity')  # 사용자가 선택한 활동

        if condition and activity:
            # ConditionActivity 모델에 저장
            ConditionActivity.objects.create(user=request.user, condition=condition, activity=activity)

        # 업로드된 파일 처리
        uploaded_file = request.FILES.get('ootd_photo')
        if uploaded_file:
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            # OOTD 모델에 저장
            OOTD.objects.create(user_profile=user_profile, image=uploaded_file)

        return redirect('weather:recommendation')  # 추천 페이지로 리다이렉트

    return render(request, 'users/upload_ootd.html')  # GET 요청 시 템플릿 렌더링

