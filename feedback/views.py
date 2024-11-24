from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        print("POST 데이터:", request.POST)  # 디버깅용
        print("FILES 데이터:", request.FILES)  # 파일 데이터 확인

        form = FeedbackForm(request.POST, request.FILES)  # request.FILES 포함
        if form.is_valid():  # 폼 검증
            feedback = form.save(commit=False)
            feedback.user = request.user  # 현재 사용자 저장
            feedback.save()  # 데이터베이스에 저장

            print("Feedback 저장 성공:", feedback)  # 디버깅용 출력
            return redirect('users:my_page')  # 제출 후 my_page로 리다이렉트
        else:
            print("폼 에러:", form.errors)  # 폼 에러 디버깅 출력
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})
