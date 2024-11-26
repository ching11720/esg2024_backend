from rest_framework.decorators import api_view
from rest_framework.response import Response
from pm.models import Resource
from ...serializers import ResourceSerializer

@api_view(['GET', 'DELETE'])
def resource_retrieve(request, RID):
    try:
        resource = Resource.objects.get(RID=RID)
    except Resource.DoesNotExist:
        return Response({'Error': 'Resource not found'}, status=404)

    if request.method == 'GET':
        if resource.status==0:
            return Response({'Error': 'Resource deleted'}, status=404)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        resource.status=0
        resource.save()
        return Response({'message': 'Source deleted successfully!'}, status=204)

    else:
        return Response({'Error': 'server error'}, status=500)