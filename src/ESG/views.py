from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from pm.models import Boundary, Employee, DailyRecord, Project, PPN
from .serializers import BoundarySerializer, SourceSerializer
from rest_framework.views import APIView
from django.db.models import Q
import re
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta

class BoundaryView(APIView):
    def post(self, request, *args, **kwargs):
        postal_code = re.findall('\d+', request.data.get('address', ''))[0]
        postal_code = postal_code.zfill(6)
        b_count = Boundary.objects.count() 
        BID = f"04{postal_code}{b_count:03d}"
        EID = request.data.get('eid')
        employee = Employee.objects.get(EID=EID)
        request.data['BID'] = BID
        today = datetime.today()
        serializer = BoundarySerializer(data=request.data)
        if serializer.is_valid():
            boundary = Boundary.objects.create(
                BID=serializer.validated_data['BID'],
                name=serializer.validated_data['name'],
                address=serializer.validated_data['address'],
                type=serializer.validated_data['type'],
                created_by=employee,
                created_date=today,
                modified_by=employee,
                modified_date=today
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
            address=request.data.get('address'),
            modified_by=request.data.get('eid'),
            modified_date=datetime.today()
        )
        boundary = Boundary.objects.get(BID=bid)
        serializer = BoundarySerializer(boundary)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        bid = request.data.get('BID')
        boundary = Boundary.objects.get(BID=bid).delete()
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

class GetPNView(APIView):
    def get(self, request, *args, **kwargs):
        ppn = PPN.objects.all().values('PN', 'name')
        ppn_list = [{'pn': PPN['PN'], 'name': PPN['name']} for PPN in ppn]
        return Response({'data': ppn_list}, status=status.HTTP_200_OK)


class SourceView(APIView):
    def get(self, request, *args, **kwargs):
        boundary = request.data.get('bid')
        pn = request.data.get('pn')
        start_year_month = request.data.get('startDate')
        end_year_month = request.data.get('endDate')
        start_date = datetime.strptime(start_year_month, '%Y-%m')
        end_date = datetime.strptime(end_year_month, '%Y-%m')
        start_of_month = start_date.replace(day=1)
        end_of_month = end_date.replace(day=1) + timedelta(days=32)
        end_of_month = end_of_month.replace(day=1) - timedelta(days=1)
        data_queryset = DailyRecord.objects.filter(date__gte=start_of_month, date__lte=end_of_month)
        ret = []
        for data in data_queryset:
            if data.PN is pn:
                record = {}
                record['bid'] = boundary
                record['pn'] = pn
                record['year'] = str(data.data)[:4]
                record['month'] = str(data.date)[5:7]
                record['amount'] = data.amount
                record['unit'] = data.unit
                record['emmit'] = data.amount * data.current_factor
                ret.append(record)
        return Response({'data':ret}, status=status.HTTP_200_OK)


class StatementView(APIView):
    def get(self, request, *args, **kwargs):
        # turn boundarys into a list
        boundarys = []
        start_year_month = request.data.get('startDate')
        end_year_month = request.data.get('endDate') 
        start_date = datetime.strptime(start_year_month, '%Y-%m')
        end_date = datetime.strptime(end_year_month, '%Y-%m')
        start_of_month = start_date.replace(day=1)
        end_of_month = end_date.replace(day=1) + timedelta(days=32)
        end_of_month = end_of_month.replace(day=1) - timedelta(days=1)
        data_queryset = DailyRecord.objects.filter(date__gte=start_of_month, date__lte=end_of_month)
        ret = []
        for boundary in boundarys:
            try:
                check = Boundary.objects.get(BID=boundary)
            except:
                return Response({'data': ret}, status=status.HTTP_404_NOT_FOUND)
            ret.append({'bid': boundary})
        for data in data_queryset:
            PID = data.PID
            project = Project.objects.filter(PID=PID)
            BID = project.BID
            date = str(data.date)
            ym = data[:7]
            amount = data.amount
            fac = data.current_factor
            for r in ret:
                if r['bid'] != BID:
                    continue
                if ym in r:
                    r[ym] += amount * fac
                else:
                    r[ym] = amount * fac
        return Response({'data': ret}, status=status.HTTP_200_OK)

