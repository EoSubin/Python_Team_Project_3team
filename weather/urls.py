from django.urls import path
from . import views

app_name = "weather"  # 네임스페이스 추가

urlpatterns = [
    path("today-weather/", views.today_weather, name="today_weather"),
    path("recommendation/", views.recommendation_view, name="recommendation"),
]
