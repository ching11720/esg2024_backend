from django.urls import path
from .views import getDailyRecord

urlpatterns = [
    path('', getDailyRecord, name="getDailyRecord"),
]