from django.urls import path
from pm.view.daily_record.record_create import record_create
from pm.view.daily_record.record_retrieve import record_retrieve
from pm.view.usage.usage_create import usage_create
from pm.view.usage.usage_retrieve import usage_retrieve
from pm.view.works_on.member_create import mem_create
from pm.view.works_on.member_in_project import member_in_project
from pm.view.works_on.member_retrieve import member_retrieve
from pm.view.flow.flow import flow

urlpatterns = [
    path('daily_record/', record_create, name="daily_record"),
    path('daily_record/<str:PID>/<str:date>/', record_retrieve, name="daily_record_retrieve"),
    path('usage/', usage_create, name="usage_create"),
    path('usage/<str:PID>/<str:PN>/', usage_retrieve, name="equip_retrieve"),
    path('member/', mem_create, name="member_create"),
    path('member/<str:PID>/', member_in_project, name="member_in_project_retrieve"),
    path('member/<str:PID>/<str:EID>/', member_retrieve, name="member_retrieve"),
    path('flow/<str:PID>/', flow, name="flow"),
]
