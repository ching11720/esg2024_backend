from rest_framework.decorators import api_view
from rest_framework.response import Response
from pm.models import Resource
from ...serializers import ResourceSerializer

@api_view(['GET']) 
def equipment(request):
    if request.method == 'GET':
        equipment = Resource.objects.filter(status=1)
        serializer = ResourceSerializer(equipment, many=True)
        return Response(serializer.data)
    else:
        return Response({'Error': 'server error'}, status=500)