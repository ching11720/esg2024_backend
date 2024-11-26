from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import WorksOn
from ...serializers import WorkSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def member_retrieve(request, PID, EID):
    try:
        member = WorksOn.objects.get(PID=PID, EID=EID)
    except:
        return Response({'Error': 'Member not found'}, status=404)

    if request.method == 'GET':
        serializer = WorkSerializer(member)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = WorkSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Member revised successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=200)
        return Response(serializer.errors, status=505)
        
    elif request.method == 'DELETE':
        member.delete()
        return Response({'message': 'Member deleted successfully!'}, status=204)
    
    else:
        return Response({'Error': 'server error'}, status=500)