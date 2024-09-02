from rest_framework import serializers
from pm import models

class SourceSerializer(serializers.ModelSerializer):
    factor = serializers.FloatField(required=False, allow_null=True, default=0)
    form = serializers.CharField(max_length=10, required=False, allow_null=True, default='')
    category = serializers.CharField(max_length=10, required=False, allow_null=True, default='')
    class Meta:
        model = models.Source
        fields = '__all__'

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Supply
        fields = '__all__'

class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repair
        fields = '__all__'