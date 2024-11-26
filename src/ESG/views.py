from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from pm.models import Boundary, Resource
from .serializers import BoundarySerializer, SourceSerializer
from rest_framework.views import APIView
from django.db.models import Q
import re


class BoundaryView(APIView):
    def post(self, request, *args, **kwargs):
        postal_code = re.findall('\d+', request.data.get('address', ''))[0]
        postal_code = postal_code.zfill(6)
        b_count = Boundary.objects.count() 
        BID = f"04{postal_code}{b_count:03d}"
        request.data['BID'] = BID
        serializer = BoundarySerializer(data=request.data)
        if serializer.is_valid():
            boundary = Boundary.objects.create(
                BID=serializer.validated_data['BID'],
                name=serializer.validated_data['name'],
                address=serializer.validated_data['address'],
                type=serializer.validated_data['type'],
            )
            return Response({'success': True, 'BID': BID}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        bid = request.data.get('BID')
        try:
            boundary = Boundary.objects.get(BID=bid)
        except Boundary.DoesNotExist:
            return Response({'error': 'Boundary not found'}, status=status.HTTP_404_NOT_FOUND)
         
        Boundary.objects.filter(BID=bid).update(
            # name=request.data.get('name'),
            address=request.data.get('address')
        )
        boundary = Boundary.objects.get(BID=bid)
        serializer = BoundarySerializer(boundary)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        bid = request.data.get('BID')
        boundary = Boundary.objects.get(BID=bid)
        boundary.status = 0
        boundary.save()
        return Response({'success': True}, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        bid = request.query_params.get('BID', None)
        name = request.query_params.get('name', None)
        type = request.query_params.get('type', None)

        filters = Q()
        if bid:
            filters &= Q(BID=bid)
        if name:
            filters &= Q(name__icontains=name)
        if type:
            filters &= Q(type=type)

        boundarys = Boundary.objects.filter(filters)

        serializer = BoundarySerializer(boundarys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


"""
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

class SourceView(APIView):
    def post(self, request, *args, **kwargs):
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
    
    
    def put(self, request, *args, **kwargs):
        sid = request.data.get('SID')
        try:
            source = Source.objects.get(SID=sid)
        except Source.DoesNotExist:
            return Response({'error': 'Source not found'}, status=status.HTTP_404_NOT_FOUND)
         
        Source.objects.filter(SID=sid).update(
            EName=request.data.get('EName'),
            form=request.data.get('form'),
            MName=request.data.get('MName'),
            category=request.data.get('category')
        )
        serializer = SourceSerializer(source)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        sid = request.data.get('BID')
        source = Boundary.objects.get(SID=sid)
        source.status = 0
        source.save()
        return Response({'success': True}, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        ename = request.query_params.get('EName', None)
        form = request.query_params.get('form', None)
        mname = request.query_params.get('MName', None)
        category = request.query_params.get('category', None)

        filters = Q()
        if ename:
            filters &= Q(EName=ename)
        if form:
            filters &= Q(form=form)
        if mname:
            filters &= Q(MName=mname)
        if category:
            filters &= Q(category=category)

        sources = Source.objects.filter(filters)

        serializer = BoundarySerializer(sources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
"""


"""
class statement(APIView):
    def retrieve(self, request, *args, **kwargs):
    def Export(self, request, *args, **kwargs):
    
class audit(APIView):
    def internal_audit(self, request, *args, **kwargs):
    def external_audit(self, request, *args, **kwargs):
"""
