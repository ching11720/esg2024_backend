from rest_framework import serializers
from . import models

class DailyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyRecord
        fields = '__all__'

class DailyRecordModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyRecordModified
        fields = '__all__'

class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usage
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        fields = '__all__'

class MemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorksOn
        fields = '__all__'

class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['PID', 'flow']

