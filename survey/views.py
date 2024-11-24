from django.shortcuts import render, redirect
from collections import OrderedDict
from .models import Outfit
from survey.models import Dislike  # Dislike 모델을 임포트

def dislike_survey(request):
    if request.method == "POST":
        # 사용자가 선택한 싫어하는 옷들을 가져옵니다.
        disliked_outfits = request.POST.getlist("dislike")
        
        # 사용자가 로그인한 상태라면, 해당 사용자와 관련된 Dislike 객체를 저장합니다.
        if request.user.is_authenticated:
            for outfit_id in disliked_outfits:
                # 이미 저장되어 있지 않다면 싫어하는 옷을 저장
                outfit = Outfit.objects.get(id=outfit_id)  # outfit_id로 outfit 객체를 가져옵니다
                Dislike.objects.get_or_create(user=request.user, outfit=outfit)
        
        return redirect("weather:today_weather")  # 네임스페이스를 포함하여 수정

    # 모든 아웃핏을 카테고리별로 그룹화
    outfits = Outfit.objects.all().order_by("category")
    grouped_outfits = {}
    for outfit in outfits:
        grouped_outfits.setdefault(outfit.category, []).append(outfit)

    # 원하는 순서로 카테고리를 정렬
    category_order = ["outer", "top", "bottom", "other"]
    ordered_grouped_outfits = OrderedDict()
    for category in category_order:
        if category in grouped_outfits:
            ordered_grouped_outfits[category] = grouped_outfits[category]

    return render(request, "survey/dislike_survey.html", {"outfits": ordered_grouped_outfits})
