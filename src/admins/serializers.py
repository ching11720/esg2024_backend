from rest_framework import serializers
from pm.models import Employee, Project

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    access = serializers.CharField(max_length=50)

class EmployeesCreateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'gender', 'phone', 'email', 'nation', 'status']

class EmployeesSerialzer(serializers.ModelSerializer):
    # mail = serializers.EmailField(source='email')
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
        fields = ['PID', 'projectName', 'PMID']

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['PID', 'projectName']