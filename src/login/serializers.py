from rest_framework import serializers
from pm.models import WorksOn

class WorksOnSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(source='PID')

    class Meta:
        model = WorksOn
        fields = ['pid', 'position']
        
