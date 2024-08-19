from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equip_create, name="equip_create"),
    path('equipment/<str:PID>/<str:SRID>/', views.equip_retrieve, name="equip_retrieve"),
    path('material/', views.material_create, name="material_create"),
    path('material/<str:PID>/<str:SRID>/', views.material_retrieve, name="material_retrieve"),
    path('member/', views.mem_create, name="mem_create"),
    path('member/<str:PID>/<str:EID>/', views.mem_retrieve, name="mem_retrieve"),
    path('flow/<str:PID>/', views.flow, name="flow"),
    path('daily_record/', views.record_create, name="daily_record"),
    path('daily_record/<str:PID>/<str:date>/', views.record_retrieve, name="daily_record_retrieve"),
]
