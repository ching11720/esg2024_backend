from rest_framework.decorators import api_view
from rest_framework.response import Response
from pm.models import DailyRecord
from ..serializers import StatementSerializer

# Create your views here.
@api_view(['POST'])
def getDailyRecord(request):
    # print("this is statement api")
    if request.method == 'POST':
        # print ('this is POST')
        try: 
            record = dict()
            for project in request.data['PID']:
                print(project)
                try: 
                    # daily_data = DailyRecord.objects.select_related('PID', 'PN').filter(PID = project)
                    daily_data = DailyRecord.objects.filter(PID=project)
                    # print(str(daily_data.query))
                    # print("get data from model")
                    # print(daily_data)
                    serializer =  StatementSerializer(daily_data, many=True)
                    # print("format the data")
                    # print(serializer.data)
                    record[project] = serializer.data
                except Exception as e:
                    return Response({'Error': f'PID is invalid: {e}'}, status=404)
            return Response(record, status=200)
        except:
            return Response({'Error': 'statement api error'}, status=500)