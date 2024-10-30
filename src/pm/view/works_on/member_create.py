from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...serializers import WorkSerializer
from ...serializers import MemSerializer
from ...models import Employee

@api_view(['GET', 'POST'])
def mem_create(request):
    if request.method == 'GET':
        member = Employee.objects.all()
        serializer = MemSerializer(member, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.save()
            response_data = {
                'message': 'Member added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)