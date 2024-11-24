from django.db import models

class Outfit(models.Model):
    CATEGORY_CHOICES = [
        ('outer', '아우터'),
        ('top', '상의'),
        ('bottom', '하의'),
        ('other', '기타'),
    ]
    WARMTH_LEVEL_CHOICES = [
        (1, 'Level 1: 매우 더운 날씨 (30°C 이상)'),
        (2, 'Level 2: 더운 날씨 (23°C ~ 29°C)'),
        (3, 'Level 3: 선선한 날씨 (15°C ~ 22°C)'),
        (4, 'Level 4: 쌀쌀한 날씨 (5°C ~ 14°C)'),
        (5, 'Level 5: 매우 추운 날씨 (5°C 이하)'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    warmth_level = models.IntegerField(choices=WARMTH_LEVEL_CHOICES)
    is_frequent = models.BooleanField(default=False)  # is_frequent 필드 추가

    def __str__(self):
        return f"{self.get_category_display()} - {self.name} (Level {self.warmth_level})"
