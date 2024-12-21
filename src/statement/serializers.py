from pm.models import DailyRecord, Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['PID', 'pname']

class StatementSerializer(serializers.ModelSerializer):
    PName = serializers.CharField(source='PID.pname')
    PPN_name = serializers.CharField(source='PN.name')

    class Meta:
        model = DailyRecord
        fields = ['PName', 'PPN_name', 'date', 'runtime', 'amount', 'current_factor']