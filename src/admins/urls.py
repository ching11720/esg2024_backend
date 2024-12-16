from django.urls import path
from .views import CreateUserView, CreateProjectView, EmployeeView, DeleteEmployeeView, AssignAccessView, GetAccessView, GetBoundaryView
from . import views

urlpatterns = [
    path('user/create', CreateUserView.as_view(), name='create_user'),
    path('access/assign/', AssignAccessView.as_view(), name='assign_access'),
    path('project/create', CreateProjectView.as_view(), name='create_project'),
    path('employee/create/', EmployeeView.as_view(), name='employee_create'),
    path('employee/delete/', DeleteEmployeeView.as_view(), name='employee_delete'),
    path('employee/retrieve/', EmployeeView.as_view(), name='employee_retrieve'),
    path('employee/revise/', EmployeeView.as_view(), name='employee_revise'),
    path('getaccess', GetAccessView.as_view(), name='getaccess'),
    path('getboundary', GetBoundaryView.as_view(), name='getboundary')
]



