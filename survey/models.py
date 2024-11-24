from django.db import models
from django.contrib.auth.models import User
from weather.models import Outfit

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자와 연결
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)  # Outfit 항목과 연결

    def __str__(self):
        return f"{self.user.username} dislikes {self.outfit.name}"
