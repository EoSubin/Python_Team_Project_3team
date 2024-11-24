from django.shortcuts import render
from pyowm import OWM
from django.conf import settings
from .models import Outfit
from survey.models import Dislike
from users.models import ConditionActivity
from weather.models import Outfit

def get_weather_data(city="Seoul"):
    try:
        owm = OWM(settings.WEATHER_API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        return {
            "temperature": weather.temperature('celsius')["temp"],
            "min_temp": weather.temperature('celsius')["temp_min"],  # 최저 온도
            "max_temp": weather.temperature('celsius')["temp_max"],  # 최고 온도
            "status": weather.detailed_status,
            "wind_speed": weather.wind()["speed"],
            "humidity": weather.humidity,
            "precipitation": weather.rain.get('1h', 0),
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return {
            "temperature": None,
            "min_temp": None,
            "max_temp": None,
            "status": "unknown",
            "wind_speed": None,
            "humidity": None,
            "precipitation": None,
        }


def recommendation_view(request):
    # 날씨 데이터 가져오기
    weather_data = get_weather_data()
    temperature = weather_data['temperature']

    # 기본 warmth_level 설정
    warmth_level = (
        1 if temperature >= 30 else
        2 if temperature >= 23 else
        3 if temperature >= 15 else
        4 if temperature > 5 else
        5
    )

    # 사용자의 최신 ConditionActivity 가져오기
    condition_activity = ConditionActivity.objects.filter(user=request.user).last()

    # 사용자의 컨디션과 활동에 따른 레벨 조정
    if condition_activity:
        if condition_activity.condition == "감기" or condition_activity.activity == "실외":
            warmth_level = min(warmth_level + 1, 5)  # 최대 레벨은 5로 제한

    # 해당 warmth_level에 맞는 옷 추천
    recommended_outfits = Outfit.objects.filter(warmth_level=warmth_level)

    # 추천된 옷에서 사용자가 선호하지 않는 옷 제외
    disliked_outfits = Dislike.objects.filter(user=request.user)
    disliked_outfit_ids = disliked_outfits.values_list('outfit', flat=True)
    recommended_outfits = recommended_outfits.exclude(id__in=disliked_outfit_ids)

    # 카테고리별로 옷을 그룹화
    grouped_outfits = {}
    for outfit in recommended_outfits.order_by("category"):
        grouped_outfits.setdefault(outfit.category, []).append(outfit)

    # 카테고리 순서 지정
    category_order = ["outer", "top", "bottom", "other"]
    sorted_grouped_outfits = {category: grouped_outfits.get(category, []) for category in category_order}

    # 템플릿에 데이터 전달
    return render(request, 'weather/recommendation.html', {
        'weather': weather_data,
        'sorted_grouped_outfits': sorted_grouped_outfits,
        'warmth_level': warmth_level,  # 최종 레벨
    })


def today_weather(request):
    # 날씨 데이터 가져오기
    weather_data = get_weather_data()

    # 최저 온도와 최고 온도의 차이 계산
    min_temp = weather_data.get("min_temp")
    max_temp = weather_data.get("max_temp")
    temperature_difference = None
    alert_message = None

    if min_temp is not None and max_temp is not None:
        temperature_difference = max_temp - min_temp

        # 일교차가 10도 이상인 경우 알림 메시지 설정
        if temperature_difference >= 10:
            alert_message = "오늘 일교차가 유독 큰 날입니다. 옷을 신경써서 입어주세요."

    # 템플릿에 전달
    return render(request, "weather/today_weather.html", {
        "weather": weather_data,
        "alert_message": alert_message,
    })
