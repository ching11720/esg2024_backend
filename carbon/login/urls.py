from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginUserView.as_view(), name="login"),
    #path('user_info', views.UserInfoView.as_view(), name="user_info"),
    path('revise_password', views.RevisePasswordView.as_view(), name="revise_password"),
]
