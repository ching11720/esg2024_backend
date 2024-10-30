from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from pm.models import Resource
from ...serializers import ResourceSerializer

# create id
def create_id(pdate,age,nn):
    ym=pdate.strftime('%Y%m')
    RID=f"03{ym}{str(age).zfill(2)}{str(nn).zfill(4)}"
    return RID

# get the total amount of data in specific table
def total_table():
    total = Resource.objects.count()
    return total

@api_view(['POST'])
def resource_create(request):
    if request.method == 'POST':
        data=request.data
        pdate=datetime.strptime(data['purchase_date'], '%Y-%m-%d')
        age=data['age']
        RID=create_id(pdate,age,total_table()+1)
        print(RID)
        
        if data['factor'] == 'NULL':
            factor=0
        else:
            factor=float(data['factor'])
        
        ### to revise age and factor in correct format and add RID
        input1={
            'RID':RID,
            'name':data['name'],
            'PN':data['PN'],
            'amount':data['amount'],
            'unit':data['unit'],
            'purchase_date':data['purchase_date'],
            'disposal_date':data['disposal_date'],
            'age':int(age),
            'SID':data['SID'],
            'factor':factor,
            'form':data['form'],
            'category':data['category'],
            'status':data['status'],
        }
        serializer = ResourceSerializer(data=input1)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Source added successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=505)
    
    else:
        return Response({'Error': 'server error'}, status=500)