from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...serializers import UsageSerializer
from ...models import Usage


@api_view(['GET', 'DELETE', 'PUT'])
def usage_retrieve(request, PID, PN):
    try:
        usage = Usage.objects.get(PN=PN, PID=PID)
    except:
        return Response({'Error': 'Usage not found'}, status=404)

    if request.method == 'GET':
        serializer = UsageSerializer(usage)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        usage.delete()
        return Response({'message': 'Source deleted successfully!'}, status=204)
    
    elif request.method == 'PUT':
        serializer = UsageSerializer(usage, data=request.data)
        if serializer.is_valid():
            updated_instance = serializer.update(usage, serializer.validated_data)
            response_data = {
                'message': 'Material updated successfully!',
                'data': UsageSerializer(updated_instance).data,
            }
            return Response(response_data, status=200)
        return Response(serializer.errors, status=505)
        
    else:
        return Response({'Error': 'server error'}, status=500)