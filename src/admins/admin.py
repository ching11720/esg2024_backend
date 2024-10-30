from django.contrib import admin
from pm.models import Employee, Project, WorksOn

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(WorksOn)