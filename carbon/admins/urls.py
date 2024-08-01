from django.urls import path
from . import views

urlpatterns = [
    path('create_user', views.create_user, name="create_user"),
    path('create_project', views.create_project, name="create_project"),
    path('employees/', views.employee_management, name='employee-management'),
    path('employee/<str:eid>', views.employee, name="employee_management"),
]
