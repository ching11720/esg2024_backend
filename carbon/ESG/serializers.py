from rest_framework import serializers
from .models import Boundary, Source


class BoundarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Boundary
        fields = ['BID', 'bname', 'gender', 'address', 'type']



class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['SID', 'ename', 'form', 'mname', 'category']