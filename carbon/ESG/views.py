from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from .models import Boundary, Source
from .serializers import BoundarySerializer, SourceSerializer
from rest_framework.views import APIView
from datetime import datetime
"""
class boundary(APIView):
    def post(self, request, *args, **kwargs):
        postal_code = request.data.get('postal_code')
        b_count = Boundary.Objects.count() #+ 1
        BID = f"05{postal_code}{b_count:03d}"
        request.data['BID'] = BID
        serializer = BoundarySerializer(data=request.data)
        if serializer.is_valid():
            boundary = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            boundary = Boundary.objects.get(BID=BID)
        except Boundary.DoesNotExist:
            return Response({'error': 'Boundary not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeesSerialzer(employee, data=request.data)
        pid = request.data.get('PID', None)      
        if serializer.is_valid():
            Employee.objects.filter(EID=EID).update(
                name=serializer.validated_data['name'],
                gender=serializer.validated_data['gender'],
                phone=serializer.validated_data['phone'],
                email=serializer.validated_data['email'],
                nation=serializer.validated_data['nation'],
                status=1
            )
            if pid:
                try:
                    employee = Employee.objects.get(EID=EID)
                    project = Project.objects.get(PID=pid)
                    WorksOn.objects.create(EID=employee, PID=project, position="Default Position")
                except Project.DoesNotExist:
                    return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, *args, **kwargs):
        if(request.method == 'DELETE'):
            bid = request.Post['BID']
            db = connect_db()
            cursor = db.cursor()
            delete = 'UPDATE FROM borders SET status = 0 WHERE BID = {}'.format(bid)
            cursor.execute(delete)
            db.commit()
            db.close()
            return Response('success')
    
    def get(self, request, *args, **kwargs):
        if(request.method == 'GET'):
            conditions = [request.Post['BID'], request.Post['name'], request.Post['type']]
            db = connect_db()
            cursor = db.cursor()
            retrieve = 'SELECT * FROM borders WHERE 1=1'
            param = []
            if request.Post['BID'] is not None:
                retrieve += ' AND BID = %s'
                param.append(conditions[0])
            if request.Post['name'] is not None:
                retrieve += ' AND name = %s'
                param.append(conditions[1])
            if request.Post['type'] is not None:
                retrieve += ' AND type = %s'
                param.append(conditions[2])
            cursor.execute(retrieve, param)
            result = cursor.fetchall()
            db.close()
            return Response(result)

"""
"""
class source():
    def Post(self, request, *args, **kwargs):
        serializer = SourceSerializer(data=request.data)
        # get MID
    def put():
    def delete():
    def get():


class statement():
    def retrieve():
    def Export():
    
class audit():
    def internal_audit():
    def external_audit():
"""
