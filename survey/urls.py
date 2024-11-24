from django.urls import path
from . import views

urlpatterns = [
    path("dislike_survey/", views.dislike_survey, name="dislike_survey"),
]
