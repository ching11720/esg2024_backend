from rest_framework import serializers
from .models import Employee#, Project

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    permission = serializers.CharField(max_length=50)
"""
class EmployeesCreateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'gender', 'phone', 'email', 'nation', 'status']

class EmployeesSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['EID', 'name', 'gender', 'phone', 'email', 'nation', 'status']

class EmployeesDeleteSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['EID', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['PID', 'pname', 'PMID']"""