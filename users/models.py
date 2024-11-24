from django.contrib.auth.models import User
from django.db import models
from weather.models import Outfit  # 올바른 참조 경로

# 사용자 프로필 모델
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avoid_categories = models.ManyToManyField(Outfit, related_name='avoided_by', blank=True)

    def __str__(self):
        return self.user.username

# 사용자 상태 및 활동 모델
class ConditionActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(
        max_length=100,
        choices=[('보통', '보통'), ('감기', '감기')],
    )
    activity = models.CharField(
        max_length=100,
        choices=[('실내', '실내'), ('실외', '실외')],
    )

    def __str__(self):
        return f"{self.user.username}: {self.get_condition_display()} / {self.get_activity_display()}"

# OOTD 모델
class OOTD(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='ootds', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ootd_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
