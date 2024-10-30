from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...serializers import DailyRecordSerializer
from ...models import DailyRecord

@api_view(['GET'])
def record_retrieve(request, PID, date):
    try:
        records = DailyRecord.objects.all().filter(PID=PID, date=date)
    except:
        return Response({'Error': 'Record not found!'}, status=404)

    #can get many records
    if request.method == 'GET':
        serializer = DailyRecordSerializer(records, many=True)
        return Response(serializer.data)
    
    #can only modify one record
    # elif request.method == 'PUT':
    #     data = add_creator_or_modifier(request.data, 0)
    #     data['status'] = 0       #means that the permission should be sent to manager
    #     serializer = serializers.DailyRecordModifySerializer(data=data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         response_data = {
    #             'message': 'Record updated successfully!',
    #             'data': serializer.data,
    #         }
    #         return Response(response_data, status=200)
    #     return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)