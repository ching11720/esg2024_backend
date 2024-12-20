from django.urls import path
from .view.statement import getDailyRecord
from .view.get_all_project import get_all_project

urlpatterns = [
    path('', getDailyRecord, name="getDailyRecord"),
    path('project/', get_all_project, name="get_all_project"),
]