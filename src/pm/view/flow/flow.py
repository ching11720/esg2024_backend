from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Project
from ...serializers import FlowSerializer

@api_view(['GET', 'PUT'])
def flow(request, PID):
    try:
        flow = Project.objects.only('PID', 'flow').get(PID=PID)
    except:
        return Response({'Error': 'PID is invalid'}, status=404)

    if request.method == 'GET':
        serializer = FlowSerializer(flow)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FlowSerializer(flow, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Flow added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)
