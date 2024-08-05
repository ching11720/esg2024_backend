from django.urls import path
from .views import LoginUserView, RevisePasswordView,CheckOldPasswordView

urlpatterns = [
    path('', LoginUserView.as_view(), name='login'),
    path('check_old_password', CheckOldPasswordView.as_view(), name='check_old_password'),
    path('revise_password', RevisePasswordView.as_view(), name="revise_password"),
]
