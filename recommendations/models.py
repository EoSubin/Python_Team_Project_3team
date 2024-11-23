from django.db import models
from django.contrib.auth.models import User

class Outfit(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('outer', 'Outerwear'),
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    warmth_level = models.IntegerField()

    def __str__(self):
        return self.name


class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avoid_categories = models.ManyToManyField(Outfit, related_name='avoided_by')

    def __str__(self):
        return f"Preferences for {self.user.username}"


class WeatherRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)

    def __str__(self):
        return f"Record for {self.user.username} - {self.outfit.name}"
