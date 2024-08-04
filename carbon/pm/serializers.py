from rest_framework import serializers
from . import models

class EQUsageSerializer(serializers.Serializer):
    class Meta:
        model = models.Usage
        fields = ['PID', 'EQID', 'amount', 'unit']

class MUsageSerializer(serializers.Serializer):
    class Meta:
        model = models.Usage
        fields = ['PID', 'MID', 'amount', 'unit']

class EQSerializer(serializers.Serializer):
    class Meta:
        model = models.Equipment
        fields = '__all__'

class MSerializer(serializers.Serializer):
    class Meta:
        model = models.Material
        fields = '__all__'

class MemSerializer(serializers.Serializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class WorkSerializer(serializers.Serializer):
    class Meta:
        model = models.WorksOn
        fields = '__all__'

class FlowSerializer(serializers.Serializer):
    class Meta:
        model = models.Project
        fields = ['PID', 'flow']
