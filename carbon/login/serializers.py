from rest_framework import serializers
from pm.models import WorksOn

class WorksOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksOn
        fields = ['EID', 'PID', 'position']
