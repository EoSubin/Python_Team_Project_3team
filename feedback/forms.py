from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['satisfaction', 'ootd_photo']  # 업로드 필드 포함
