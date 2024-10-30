from rest_framework.decorators import api_view
from rest_framework.response import Response
from pm.models import Resource
from ...serializers import ResourceSerializer

@api_view(['GET'])
def material(request):
    if request.method == 'GET':
        material = Resource.objects.filter(status=2)
        serializer = ResourceSerializer(material, many=True)
        return Response(serializer.data)
    else:
        return Response({'Error': 'server error'}, status=500)