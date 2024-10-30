from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import WorksOn
from ...serializers import WorkSerializer

@api_view(['GET'])
def member_in_project(request, PID):
    if request.method == 'GET':
        try:
            member = WorksOn.objects.all().filter(PID=PID)
        except:
            return Response({'Error': "There's no member in this project"}, status=404)
        serializer = WorkSerializer(member, many=True)
        return Response(serializer.data)
    else:
        return Response({'Error': 'server error'}, status=500)