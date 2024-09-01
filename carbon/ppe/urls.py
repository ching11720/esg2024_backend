from django.urls import path
from . import views

urlpatterns = [
    path('source/', views.source_create, name="source_create"),
    path('source/<str:SRID>/', views.source_retrieve, name="source_retrieve"),
    path('material/', views.material, name="material_view"),
    path('equipment/', views.equipment, name="equipment_view"),
    path('disposal/', views.equipment_disposal, name="equipment_disposal"),
    path('repair_log/', views.repair_log, name="repair_log"),
]