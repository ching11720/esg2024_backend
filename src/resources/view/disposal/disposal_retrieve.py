from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from pm.models import Resource
from ...serializers import ResourceSerializer

@api_view(['GET'])
def equipment_disposal(request):
    if request.method == 'GET':
        now = datetime.now()
        next_halfyr = now + timedelta(days=180)
        source = Resource.objects.filter(disposal_date__lte=next_halfyr, status=1)
        if not source:
            return Response({'message': 'No disposal item recently'}, status=205)
        serializer = ResourceSerializer(source, many=True)
        return Response(serializer.data)
    else:
        return Response({'Error': 'server error'}, status=500)