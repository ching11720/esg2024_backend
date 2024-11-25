from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...serializers import DailyRecordSerializer
from datetime import datetime

@api_view(['POST'])
def record_create(request):
    if request.method == 'POST':
        now = datetime.now()
        request.data['created_by'] = '022024040210'
        request.data['created_date'] = now.strftime('%Y-%m-%d')
        request.data['last_modified_by'] = '022024040210'
        request.data['last_modified_date'] = now.strftime('%Y-%m-%d')
        ## todo
        request.data['current_factor'] = 0

        serializer = DailyRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Record added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)