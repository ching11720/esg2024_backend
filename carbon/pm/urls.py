from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equip_create, name="equip_create"),
    path('equipment/<str:EQID>/', views.equip_retrieve, name="equip_retrieve"),
    path('material/', views.material_create, name="material_create"),
    path('material/<str:MID>/', views.material_retrieve, name="material_retrieve"),
    path('member/', views.mem_create, name="mem_create"),
    path('member/<str:EID>/', views.mem_retrieve, name="mem_retrieve"),
    path('flow/', views.flow, name="flow"),
    #path('/Project_Manager/Statement', views.stat, name="stat"),
    #path('daily_record', views.daily_record, name="daily_record"),
]
