from weather.models import Outfit  # 여기서만 임포트
from survey.models import Dislike

def get_outfits_based_on_weather(temperature, user):
    # 기온에 따른 기본 추천 Level
    warmth_level = 1 if temperature >= 30 else 2 if temperature >= 23 else 3 if temperature >= 15 else 4 if temperature > 5 else 5

    # 해당 레벨에 맞는 옷 추천
    recommended_outfits = Outfit.objects.filter(warmth_level=warmth_level)

    # 사용자가 싫어하는 옷을 제외
    disliked_outfits = Dislike.objects.filter(user=user)
    disliked_outfit_ids = disliked_outfits.values_list('outfit', flat=True)
    recommended_outfits = recommended_outfits.exclude(id__in=disliked_outfit_ids)

    return recommended_outfits
