from django.urls import path
from . import views

urlpatterns = [
    path('daily_record/', views.record_create, name="daily_record"),
    path('daily_record/<str:PID>/<str:date>/', views.record_retrieve, name="daily_record_retrieve"),
    path('flow/<str:PID>/', views.flow, name="flow"),
    path('member/', views.mem_create, name="member_create"),
    path('member/<str:PID>/', views.mem_p_list, name="member_in_project_retrieve"),
    path('member/<str:PID>/<str:EID>/', views.mem_retrieve, name="member_retrieve"),
    path('usage/', views.usage_create, name="usage_create"),
    path('usage/<str:PID>/<str:PN>/', views.usage_retrieve, name="equip_retrieve"),
]
