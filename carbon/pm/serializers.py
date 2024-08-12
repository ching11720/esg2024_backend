from rest_framework import serializers
from . import models

class EQUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsageEq
        fields = '__all__'

class MUsageMSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsageM
        fields = '__all__'

class MUsageSerializer(serializers.Serializer):
    class Meta:
        model = models.UsageM
        fields = '__all__'
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class EQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = '__all__'

class MSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
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
