from django.urls import path
from . import views

app_name = 'users'  # 네임스페이스 설정

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('my-page/', views.my_page_view, name='my_page'),
    path('upload-ootd/', views.upload_ootd_view, name='upload_ootd'),
]
