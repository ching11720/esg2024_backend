from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...serializers import UsageSerializer

@api_view(['POST'])
def usage_create(request):
    if request.method == 'POST':
        serializer = UsageSerializer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            # print("valid")
            serializer.save()
            # print("saved")
            response_data = {
                'message': 'Usage added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)