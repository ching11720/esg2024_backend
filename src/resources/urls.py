from django.urls import path
from resources.view.getall_equipment.getall_equipment import equipment
from resources.view.getall_material.getall_material import material
from resources.view.resource.resource_create import resource_create
from resources.view.resource.resource_retrieve import resource_retrieve
from resources.view.disposal.disposal_retrieve import equipment_disposal
from resources.view.repair.repair_log import repair_log

urlpatterns = [
    path('equipment/', equipment, name="equipment_view"),
    path('material/', material, name="material_view"),
    path('create/', resource_create, name="resource_create"),
    path('retrieve/<str:RID>/', resource_retrieve, name="resource_retrieve"),
    path('disposal/', equipment_disposal, name="equipment_disposal"),
    path('repair_log/', repair_log, name="repair_log"),
]