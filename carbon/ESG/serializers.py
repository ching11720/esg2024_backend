from rest_framework import serializers
from pm.models import Boundary, Source


class BoundarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Boundary
        fields = ['BID', 'name', 'address', 'type']



class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['SID', 'ename', 'form', 'mname', 'category']