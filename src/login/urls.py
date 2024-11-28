from django.urls import path
from .views import LoginUserView, UserInfoView, RevisePasswordView

urlpatterns = [
    path('', LoginUserView.as_view(), name="login"),
    path('user_info', UserInfoView.as_view(), name="user_info"),
    path('revise_password', RevisePasswordView.as_view(), name="revise_password"),
]
