from django.contrib import admin
from .models import Feedback
from django.utils.html import format_html

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'satisfaction', 'temperature_level', 'photo_preview', 'created_at')

    def photo_preview(self, obj):
        if obj.ootd_photo:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.ootd_photo.url)
        return "No Image"

    photo_preview.short_description = "OOTD Photo"
