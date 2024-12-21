from rest_framework.decorators import api_view
from rest_framework.response import Response
from pm.models import Project
from ..serializers import ProjectSerializer

@api_view(['GET'])
def get_all_project(request):
    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=200)
    else:
        return Response({'Error': 'get project api error'}, status=500)