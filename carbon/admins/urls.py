from django.urls import path
from .views import CreateUserView#, CreateProjectView, EmployeeView, DeleteEmployeeView, AssignAccessView
from . import views

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    # path('assign_access/', AssignAccessView.as_view(), name='assign_access'),
    # path('create_project/', CreateProjectView.as_view(), name='create_project'),
    # path('employee/create/', EmployeeView.as_view(), name='employee_create'),
    # path('employee/delete/', DeleteEmployeeView.as_view(), name='employee_delete'),
    # path('employee/retrieve/', EmployeeView.as_view(), name='employee_retrieve'),
    # path('employee/revise/', EmployeeView.as_view(), name='employee_revise'),
]


