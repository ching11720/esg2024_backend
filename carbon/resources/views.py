from pm import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from django.db import connection
from datetime import datetime, timedelta

# get the total amount of data in specific table
def total_table():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM `source`")
        total = cursor.fetchone()[0]
    return total

# create id
def create_id(pdate,age,nn):
    ym=pdate.strftime('%Y%m')
    SRID=f"03{ym}{str(age).zfill(2)}{str(nn).zfill(4)}"
    return SRID

# Create your views here.
@api_view(['POST'])
def resource_create(request):
    if request.method == 'POST':
        data=request.data
        pdate=datetime.strptime(data['purchase_date'], '%Y-%m-%d')
        age=data['age']
        SRID=create_id(pdate,age,total_table()+1)
        print(SRID)
        
        if data['factor'] == 'NULL':
            factor=0
        else:
            factor=float(data['factor'])
        
        input1={
            'SRID':SRID,
            'name':data['name'],
            'amount':data['amount'],
            'unit':data['unit'],
            'purchase_date':data['purchase_date'],
            'disposal_date':data['disposal_date'],
            'age':int(age),
            'factor':factor,
            'form':data['form'],
            'category':data['category'],
            'status':data['status'],
        }
        input2={
            'SRID':SRID,
            'SID':data['SID'],
        }
        serializer1 = serializers.SourceSerializer(data=input1)
        if serializer1.is_valid():
            serializer1.save()
            response_data = {
                'message': 'Source added successfully!',
                'data': serializer1.data,
            }
            serializer2 = serializers.SupplySerializer(data=input2)
            if serializer2.is_valid():
                serializer2.save()
                return Response(response_data, status=201)
        errors = {
            'source_add_errors': serializer1.errors,
            'supply_add_errors': serializer2.errors,
        }
        return Response(errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'DELETE'])
def resource_retrieve(request, SRID):
    try:
        source = models.Source.objects.get(SRID=SRID)
    except models.Source.DoesNotExist:
        return Response({'Error': 'Source not found'}, status=404)

    if request.method == 'GET':
        serializer = serializers.SourceSerializer(source)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        source.status=0
        source.save()
        return Response({'message': 'Source deleted successfully!'}, status=204)

    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET'])
def material(request):
    if request.method == 'GET':
        material = models.Source.objects.filter(status=2)
        serializer = serializers.SourceSerializer(material, many=True)
        return Response(serializer.data)
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET']) 
def equipment(request):
    if request.method == 'GET':
        equipment = models.Source.objects.filter(status=1)
        serializer = serializers.SourceSerializer(equipment, many=True)
        return Response(serializer.data)
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET'])
def equipment_disposal(request):
    if request.method == 'GET':
        now=datetime.now()
        next_halfyr=now + timedelta(days=180)
        source=models.Source.objects.filter(disposal_date__lte=next_halfyr, status=1)
        if not source:
            return Response({'message': 'No disposal item recently'}, status=205)
        serializer = serializers.SourceSerializer(source, many=True)
        return Response(serializer.data)
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'POST'])
def repair_log(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            # now=datetime.now()
            # past_halfyr=now - timedelta(days=180)
            cursor.execute("SELECT * FROM `repairs`")
            rows = cursor.fetchall()
            if rows:
                columns = ['SRID', 'repair_date', 'notes']
                repair = [dict(zip(columns, row)) for row in rows]
        return Response(repair)

    elif request.method == 'POST':
        data=request.data
        serializer = serializers.RepairSerializer(data=data)
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

