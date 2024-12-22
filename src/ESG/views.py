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
import datetime
import logging

logger = logging.getLogger('ESG')

class BoundaryView(APIView):
    def post(self, request, *args, **kwargs):
        postal_code = re.findall('\d+', request.data.get('address', ''))[0]
        postal_code = postal_code.zfill(6)
        b_count = Boundary.objects.count() 
        BID = f"04{postal_code}{b_count:03d}"
        EID = request.data.get('EID')
        employee = Employee.objects.get(EID=EID)
        request.data['BID'] = BID
        today = datetime.datetime.today()
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
         
        Boundary.objects.get(BID=bid).update(
            # name=request.data.get('name'),
            address=request.data.get('address'),
            modified_by=request.data.get('EID'),
            modified_date=datetime.datetime.today()
        )
        boundary = Boundary.objects.get(BID=bid)
        serializer = BoundarySerializer(boundary)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        bid = request.data.get('BID')
        try:
            boundary = Boundary.objects.get(BID=bid)
            boundary.delete()
        except:
            return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
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
        return Response(ppn_list, status=status.HTTP_200_OK)


class SourceView(APIView):
    def post(self, request, *args, **kwargs):
        boundary = request.data.get('bid')
        pn = request.data.get('pnid')
        today = str(datetime.datetime.today())[:10]
        start = today[:4] + '-01-01'
        start_year_month = request.data.get('startDate', start)
        end_year_month = request.data.get('endDate', today) 
        start_date = datetime.datetime.strptime(start_year_month, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_year_month, '%Y-%m-%d')
        start_of_month = start_date.replace(day=1)
        end_of_month = end_date.replace(day=1) + datetime.timedelta(days=32)
        end_of_month = end_of_month.replace(day=1) - datetime.timedelta(days=1)
        data_queryset = DailyRecord.objects.filter(date__gte=start_of_month, date__lte=end_of_month)
        ret = []
        for data in data_queryset:
            if data.PN.PN == pn:
                record = {}
                record['bid'] = boundary
                record['pn'] = pn
                record['year'] = str(data.date)[:4]
                record['month'] = str(data.date)[5:7]
                record['amount'] = data.amount
                record['unit'] = data.unit
                record['emmit'] = data.amount * data.current_factor
                ret.append(record)
        return Response(ret, status=status.HTTP_200_OK)


class StatementView(APIView):
    def post(self, request, *args, **kwargs):
        boundarys = request.data.get('selecedtBoundary', [])
        today = str(datetime.datetime.today())[:10]
        start = today[:4] + '-01-01'
        start_year_month = request.data.get('startDate', start)
        end_year_month = request.data.get('endDate', today) 
        start_date = datetime.datetime.strptime(start_year_month, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_year_month, '%Y-%m-%d')
        start_of_month = start_date.replace(day=1)
        end_of_month = end_date.replace(day=1) + datetime.timedelta(days=32)
        end_of_month = end_of_month.replace(day=1) - datetime.timedelta(days=1)
        data_queryset = DailyRecord.objects.filter(date__gte=start_of_month, date__lte=end_of_month)
        ret = []
        logger.debug(f'startDate: {start_year_month}')
        logger.debug(f'endDate: {end_year_month}')
        '''
        today = str(datetime.datetime.today())[:7]
        start = today[:4] + '-01'
        start_year_month = request.query_params.get('startDate', start)
        end_year_month = request.query_params.get('endDate', today) 
        start_date = datetime.datetime.strptime(start_year_month, '%Y-%m').date()
        end_date = datetime.datetime.strptime(end_year_month, '%Y-%m').date
        logger.debug(f'startDate: {start_date}, endDate: {end_date}')
        data_queryset = DailyRecord.objects.filter(date__gte=start_date, date__lte=date)
        '''
        for boundary in boundarys:
            try:
                check = Boundary.objects.get(BID=boundary)
            except:
                return Response({'data': ret}, status=status.HTTP_404_NOT_FOUND)
            ret.append({'bid': boundary})
        for data in data_queryset:
            project = data.PID
            boundary = project.BID
            date = str(data.date)
            ym = date[:7]
            amount = data.amount
            factor = data.current_factor
            for r in ret:
                if r['bid'] != boundary.BID:
                    continue
                if ym in r:
                    r[ym] += amount * factor
                else:
                    # r[ym] = 0
                    r[ym] = amount * factor
        return Response({'data': ret}, status=status.HTTP_200_OK)

