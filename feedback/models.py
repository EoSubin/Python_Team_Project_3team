from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    satisfaction = models.IntegerField(choices=[(1, 'Cold'), (2, 'Neutral'), (3, 'Hot')])
    ootd_photo = models.ImageField(upload_to='feedback_photos/', null=True, blank=True)  # 피드백 이미지
    temperature_level = models.IntegerField(choices=[
        (1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Level 4'), (5, 'Level 5')
    ], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간 추가

    def __str__(self):
        return f"Feedback by {self.user.username}"
