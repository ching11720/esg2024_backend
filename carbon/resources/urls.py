from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equipment, name="equipment_view"),
    path('material/', views.material, name="material_view"),
    path('create/', views.resource_create, name="resource_create"),
    path('retrieve/<str:SRID>/', views.resource_retrieve, name="resource_retrieve"),
    path('disposal/', views.equipment_disposal, name="equipment_disposal"),
    path('repair_log/', views.repair_log, name="repair_log"),
]