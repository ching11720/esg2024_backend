from django.urls import path
from . import views
from views import LoginUserView, RevisePasswordView

urlpatterns = [
    path('', LoginUserView.as_view(), name="login"),
    path('revise_password', RevisePasswordView.as_view(), name="revise_password"),
]
