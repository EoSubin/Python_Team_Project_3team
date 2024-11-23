from django.shortcuts import render, redirect
from .models import *
from .forms import FeedbackForm
from django.conf import settings
from pyowm import OWM

# 날씨 데이터를 가져오는 함수
def get_weather_data(city="Seoul"):
    owm = OWM(settings.WEATHER_API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temperature = weather.temperature('celsius')["temp"]
    status = weather.detailed_status
    wind_speed = weather.wind()["speed"]
    humidity = weather.humidity
    precipitation = weather.rain.get('1h', 0)

    return {
        "temperature": temperature,
        "status": status,
        "wind_speed": wind_speed,
        "humidity": humidity,
        "precipitation": precipitation
    }

# 추천 로직 (옷 추천과 피드백 처리)
def recommendations_view(request):
    # 사용자 기본값 설정
    user_pref = None
    avoid_categories = []

    # 로그인 여부 확인 및 사용자 설정 불러오기
    if request.user.is_authenticated:
        user_pref, created = UserPreference.objects.get_or_create(user=request.user)
        avoid_categories = user_pref.avoid_categories.all()

    # 날씨 데이터 가져오기
    weather_data = get_weather_data()
    temperature = weather_data["temperature"]
    conditions = weather_data["status"]

    # 기온에 따른 추천 Level 설정
    if temperature >= 30:
        warmth_level = 1
    elif temperature >= 23:
        warmth_level = 2
    elif temperature >= 15:
        warmth_level = 3
    elif temperature >= 5:
        warmth_level = 4
    else:
        warmth_level = 5

    # 날씨 조건에 따른 추가 조정
    if "rain" in conditions.lower():
        warmth_level += 1
    elif "snow" in conditions.lower():
        warmth_level += 2

    # 추천 옷 필터링
    exclude_ids = avoid_categories.values_list('id', flat=True)
    recommended_outfits = Outfit.objects.filter(warmth_level=warmth_level).exclude(id__in=exclude_ids)

    # 피드백 처리
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            for outfit in recommended_outfits:
                weather_record, created = WeatherRecord.objects.get_or_create(user=request.user, outfit=outfit)
                weather_record.feedback = feedback
                weather_record.save()
            return redirect('recommendations')  # 성공적으로 제출한 후 페이지 리로드
    else:
        form = FeedbackForm()

    # 템플릿에 데이터 전달
    return render(request, 'recommendations/recommendation.html', {
        'outfits': recommended_outfits,
        'weather': weather_data,  # 날씨 데이터를 weather 키로 전달
        'form': form,
    })
