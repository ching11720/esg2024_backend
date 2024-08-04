from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers

# Create your views here.
'''
def daily_record(request):
    if request.method == 'POST':
        date = request.POST['date']
        equipment = request.POST['equipment']
        material = request.POST['material']
        eqmamount = request.POST['eqmamount']
        eqmunit = request.POST['eqmunit']
        matamount = request.POST['matamount']
        matunit = request.POST['matunit']
        runtime = request.POST['runtime']
    
    elif request.method == 'RETRIEVE':
        date = request.POST['date']
    elif request.method == 'REVISE':
        date = request.POST['date']
        equipment = request.POST['equipment']
        material = request.POST['material']
        eqmamount = request.POST['eqmamount']
        eqmunit = request.POST['eqmunit']
        matamount = request.POST['matamount']
        matunit = request.POST['matunit']
        runtime = request.POST['runtime']
'''

@api_view(['GET', 'POST'])
def equip_create(request):
    if request.method == 'GET':
        equipment = models.Equipment.objects.all()
        serializer = serializers.EQSerializer(equipment, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.EQUsageSerializer(data=request.data)
        if serializer.is_valid():
            equipment = serializer.save()
            response_data = {
                'message': 'Equipment added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'DELETE'])
def equip_retrieve(request, EQID):
    try:
        equipment = models.Usage.objects.only('PID', 'EQID', 'amount', 'unit').get(EQID=EQID)
    except models.Usage.DoesNotExist:
        return Response({'Error': 'Equipment not found'}, status=404)

    if request.method == 'GET':
        serializer = serializers.EQSerializer(models.Equipment.objects.get(EQID=EQID))
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        equipment.delete()
        return Response({'message': 'Food item deleted successfully!'}, status=204)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'POST'])
def material_create(request):
    if request.method == 'GET':
        material = models.Material.objects.all()
        serializer = serializers.MSerializer(material, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.MUsageSerializer(data=request.data)
        if serializer.is_valid():
            material = serializer.save()
            response_data = {
                'message': 'Material added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    
    else:
        return Response({'Error': 'server error'}, status=500)

@api_view(['GET', 'PUT'])
def material_retrieve(request, MID):
    try:
        material = models.Usage.objects.only('PID', 'MID', 'amount', 'unit').get(MID=MID)
    except models.Usage.DoesNotExist:
        return Response({'Error': 'Material not found'}, status=404)

    if request.method == 'GET':
        serializer = serializers.MSerializer(models.Material.objects.get(MID=MID))
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = serializers.MUsageSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Material deleted successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=200)
        return Response(serializer.errors, status=400)
    
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

@api_view(['GET', 'PUT', 'DELETE'])
def mem_retrieve(request, EID):
    try:
        member = models.WorksOn.objects.get(EID=EID)
    except models.WorksOn.DoesNotExist:
        return Response({'Error': 'Member not found'}, status=404)

    if request.method == 'GET':
        serializer = serializers.MemSerializer(models.Employee.objects.get(EID=EID))
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = serializers.WorkSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Member revised successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=200)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        member.delete()
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