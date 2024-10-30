from rest_framework.decorators import api_view
from rest_framework.response import Response
from pm.models import RepairLog
from ...serializers import RepairSerializer

@api_view(['GET', 'POST'])
def repair_log(request):
    if request.method == 'GET':
        try:
            repair = RepairLog.objects.all()
        except RepairLog.DoesNotExist:
            return Response({'Error': 'There is no repair log'}, status=404)
        
        serializer = RepairSerializer(repair, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data=request.data
        serializer = RepairSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Repair log added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)

