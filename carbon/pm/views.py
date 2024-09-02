from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from django.db import connection

@api_view(['POST'])
def usage_create(request):
    if request.method == 'POST':
        serializer = serializers.UsageSerializer(data=request.data)
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

@api_view(['GET', 'DELETE', 'PUT'])
def usage_retrieve(request, PID, SRID):
    print(PID, SRID)
    try:
        # equipment = models.Usage.objects.filter(SRID=SRID, PID=PID)
        with connection.cursor() as cursor:
            print("connected")
            cursor.execute('''SELECT PID,source.SRID,name,`usage`.amount,`usage`.unit FROM `usage`,source 
                           WHERE `usage`.SRID = source.SRID AND PID = %s AND source.SRID = %s''', [PID, SRID])
            print("query executed")
            rows = cursor.fetchall()
            if rows:
                columns = ['PID', 'SRID', 'name', 'amount', 'unit']
                equipment = [dict(zip(columns, row)) for row in rows]
            else:
                return Response({'Error': 'Source not found'}, status=404)
    except:
        return Response({'Error': 'server error'}, status=500)

    if request.method == 'GET':
        return Response(equipment)
    
    elif request.method == 'DELETE':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM `usage` WHERE PID = %s AND SRID = %s", [PID, SRID])
        return Response({'message': 'Source deleted successfully!'}, status=204)
    
    elif request.method == 'PUT':
        # serializer = serializers.MUsageSerializer(material, data=request.data)
        # if serializer.is_valid():
        #     updated_instance = serializer.update(material, serializer.validated_data)
        #     response_data = {
        #         'message': 'Material deleted successfully!',
        #         'data': serializers.MUsageSerializer(updated_instance).data,
        #     }
        #     return Response(response_data, status=200)
        # return Response(serializer.errors, status=400)
        data=request.data
        pid=data['PID']
        srid=data['SRID']
        amount=data['amount']
        unit=data['unit']
        if not pid or not srid or amount<0 or not unit:
            return Response({'Error': 'client error'}, status=400)
        with connection.cursor() as cursor:
            cursor.execute("UPDATE `usage` SET amount = %s, unit = %s WHERE PID = %s AND SRID = %s", [amount, unit, pid, srid])
        return Response({'message': 'Material updated successfully!', 'data': {'PID': pid, 'SRID': srid, 'amount': amount, 'unit': unit}}, status=200)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'POST'])
def mem_create(request):
    if request.method == 'GET':
        member = models.Employee.objects.all()
        serializer = serializers.MemSerializer(member, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.WorkSerializer(data=request.data)
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

@api_view(['GET'])
def mem_p_list(request, PID):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute('''SELECT employees.EID,name,PID,position,gender,email,phone,nation FROM works_on, employees 
                           WHERE works_on.EID = employees.EID AND PID = %s;''', [PID])
            # print("query executed")
            rows = cursor.fetchall()
            if rows:
                columns = ['EID', 'name', 'PID', 'position', 'gender', 'email', 'phone', 'nation']
                member = [dict(zip(columns, row)) for row in rows]
            else:
                return Response({'Error': "There's no member in this project"}, status=404)
        return Response(member)
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def mem_retrieve(request, PID, EID):
    try:
        # member = models.WorksOn.objects.get(EID=EID)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM works_on WHERE PID = %s AND EID = %s", [PID, EID])
            # print("query executed")
            rows = cursor.fetchall()
            if rows:
                columns = ['EID', 'PID', 'position']
                member = [dict(zip(columns, row)) for row in rows]
            else:
                return Response({'Error': 'Member not found'}, status=404)
        # print(member)
    except:
        return Response({'Error': 'server error'}, status=500)

    if request.method == 'GET':
        return Response(member)
    
    elif request.method == 'PUT':
        # serializer = serializers.WorkSerializer(member, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     response_data = {
        #         'message': 'Member revised successfully!',
        #         'data': serializer.data,
        #     }
        #     return Response(response_data, status=200)
        # return Response(serializer.errors, status=400)
        data=request.data
        pid=data['PID']
        eid=data['EID']
        position=data['position']
        if not pid or not eid or not position:
            return Response({'Error': 'client error'}, status=400)
        with connection.cursor() as cursor:
            cursor.execute("UPDATE works_on SET position = %s WHERE PID = %s AND EID = %s", [position, pid, eid])
        return Response({'message': 'Member updated successfully!', 'data': {'EID': eid, 'PID': pid, 'position': position}}, status=200)
    
    elif request.method == 'DELETE':
        # member.delete()
        # return Response({'message': 'Member deleted successfully!'}, status=204)
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM works_on WHERE PID = %s AND EID = %s", [PID, EID])
        return Response({'message': 'Member deleted successfully!'}, status=204)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'PUT'])
def flow(request, PID):
    try:
        flow = models.Project.objects.only('PID', 'flow').get(PID=PID)
    except:
        return Response({'Error': 'PID is invalid'}, status=401)

    if request.method == 'GET':
        serializer = serializers.FlowSerializer(flow)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = serializers.FlowSerializer(flow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Flow added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['POST'])
def record_create(request):
    if request.method == 'POST':
        serializer = serializers.RecordSerializer(data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            response_data = {
                'message': 'Record added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'PUT'])
def record_retrieve(request, PID, date):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `record` WHERE PID = %s AND date = %s", [PID, date])
            rows = cursor.fetchall()
            if rows:
                columns = ['PID', 'SRID', 'date', 'runtime', 'amount', 'unit']
                record = [dict(zip(columns, row)) for row in rows]
            else:
                return Response({'Error': 'Record not found'}, status=404)
    except:
        return Response({'Error': 'server error'}, status=500)

    if request.method == 'GET':
        return Response(record)
    
    elif request.method == 'PUT':
        data=request.data
        pid=data['PID']
        srid=data['SRID']
        date=data['date']
        runtime=data['runtime']
        amount=data['amount']
        unit=data['unit']
        if not pid or not srid or not date:
            return Response({'Error': 'client error'}, status=400)
        with connection.cursor() as cursor:
            cursor.execute("UPDATE record SET runtime = %s, amount = %s, unit = %s WHERE PID = %s AND SRID = %s AND date = %s", [runtime, amount, unit, pid, srid, date])
        return Response({'message': 'Record updated successfully!', 'data': {'PID': pid, 'SRID': srid, 'date': date, 'runtime': runtime, 'amount': amount, 'unit': unit}}, status=200)
    else:
        return Response({'Error': 'server error'}, status=500)