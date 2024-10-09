from rest_framework import serializers
from pm import models

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        fields = '__all__'

class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RepairLog
        fields = '__all__'