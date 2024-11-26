from pm.models import DailyRecord
from rest_framework import serializers

class StatementSerializer(serializers.ModelSerializer):
    PName = serializers.CharField(source='PID.pname')
    PPN_name = serializers.CharField(source='PN.name')

    class Meta:
        model = DailyRecord
        fields = ['PName', 'PPN_name', 'date', 'runtime', 'amount', 'unit', 'current_factor']