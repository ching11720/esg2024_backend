from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, EmployeesCreateSerialzer, EmployeesSerialzer
import random, string, hashlib
from datetime import datetime
from pm.models import Employee, Project, WorksOn, Boundary
from django.db.models import Q

# {"username": "test1", "permission": "admin"}

# {
#     "username": "022020112701",
#     "password": "UgNMKDNg",
#     "hashed": "586124d506bfca20c53ed0adef81e548e908ae4a5bd0f93c44bcb043ba99ca83"
# }

# {
#     "username": "022021021602",
#     "password": "NBFLc4ko",
#     "hashed": "3a73d3d6b4316445435503d2bba562be46777c3f4aa1bc9733eea01ccf08b856"
# }
# {
#     "username": "022021032503",
#     "password": "XEsUlFok",
#     "hashed": "ec5fe6c39a201830cd357429766e5894978c49582eb64ff833705fc03b170aec"
# }
# {
#     "username": "022021110504",
#     "password": "QkQsaKHd",
#     "hashed": "ea7fe60076d3beb86a9c3dd65136a7c67477c58f90cae40f491325a421ad60b0"
# }
# {
#     "username": "022022051705",
#     "password": "ccqfbD5x",
#     "hashed": "0cbd306610a1adcb2ad475c39d14f8807e507bfd5613b6e24ed90a923756cba4"
# }
# {
#     "username": "022022062106",
#     "password": "gzDmYHNQ",
#     "hashed": "49ca02ae5974326909631c29d1c7ccc5490b7d904e8bb5aee2a125bee937c939"
# }
# {
#     "username": "022022062707",
#     "password": "fDKwdzra",
#     "hashed": "fbb90e88723d2b17a4c157a5b17ac4d1ee7fe2ef8a4a0aaaa9901ab6c26c34f2"
# }
# {
#     "username": "022022070508",
#     "password": "DAVymPMd",
#     "hashed": "33083256511bb2d90bbb372f239629f9ce5063a99985a96037f549b1fb599d33"
# }
# {
#     "username": "022023050509",
#     "password": "password",
#     "hashed": "459b3b24c85be6d9cbbd21542329a8dcb44ecdc7e29b29a6b04d2e5fe54f8fd9"
# }
# {
#     "userID": "022024090010",
#     "password": "bRx3dcPm",
#     "hashed": "96fc57084a93bfd7554261c11d76a8e24e677be37d79fd93311f29a1bee8addb"
# }


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['name']
            permissions = serializer.validated_data['access']
            try:
                employee = Employee.objects.get(EID=username)
                employee.status = 2
                employee.save()
            except Employee.DoesNotExist:
                return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
            # user = User.objects.create_user(username=username, password=hashed)
            user = User(username=username)
            user.first_name = employee.name
            user.set_password(hashed)
            user.save()
            if permissions:
                group, create = Group.objects.get_or_create(name=permissions)
                user.groups.add(group)
            return Response({'userID': username, 'password': password}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignAccessView(APIView):
    def put(self, request, *args, **kwargs):
        # username = request.data.get('username')
        eid = request.data.get('name')
        permission = request.data.get('access')
        # employee = Employee.objects.get(EID=eid)
        # ename = employee.name
        try:
            user = User.objects.get(username=eid)
        except:
            return Response({'success': False}, status=status.HTTP_404_NOT_FOUND) 
        user.groups.clear()  
        group, create = Group.objects.get_or_create(name=permission)
        user.groups.add(group)
        return Response({'success': True}, status=status.HTTP_201_CREATED)
        """
        if username:
            try:
                user1 = User.objects.get(username=username)
            except:
                return Response({'fail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        if eid:
            try:
                employee = Employee.objects.get(EID=eid)
                ename = employee.name
                user2 = User.objects.get(username=ename)
            except:
                return Response({'fail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        if username and eid:
            if user1 != user2:
                return Response({'fail': 'username and userID do not match'}, status=status.HTTP_400_BAD_REQUEST)
        if username:
            user = user1
        elif eid:
            user = user2
        permissions = permissions.split(', ')
        for x in permissions:
            for x in permissions:
                try:
                    project_group = Group.objects.get(name=f'project_{x}')
                    user.groups.add(project_group)
                except:
                    return Response({'fail': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response('success', status=status.HTTP_200_OK)
        """

    
# {"pname":"project10", "PMID":"022024080009", "Material": "a, b", "Equipment": "c, d"}
class CreateProjectView(APIView):

    def post(self, request, *args, **kwargs):
        # Get the current date
        now = datetime.now()
        yy = now.strftime("%y") 
        mm = now.strftime("%m")

        # Count the number of projects created in the current month
        current_month_projects = Project.objects.filter(PID__startswith=f"01{yy}{mm}").count()
        nn = current_month_projects

        # Generate the PID
        PID = f"01{yy}{mm}{nn:02d}"
        BID = request.data.get('BID')
        # BID = Boundary.objects.get(BID='04000000000')
        # Add the generated PID to the request data
        request.data['PID'] = PID
        try:
            pmid = Employee.objects.get(EID=request.data.get('PMID'))
            #request.data['PMID'] = pmid
        except:
            return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
        project = Project.objects.create(PID=PID, pname=request.data.get('projectName'), PMID=pmid, BID=BID)
        #serializer = ProjectSerializer(data=request.data)
        #if serializer.is_valid():
            #project = serializer.save()
        #return Response('success', status=status.HTTP_201_CREATED)
        return Response({'success': True, 'PID': PID, 'PMID': pmid.EID}, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# status  3 -> account not created, 2 -> created but haven't logged in, 1 -> exist, 0 -> deleted
# {"name":"test7", "gender":1, "phone":"0912345678", "email":"a@a.com", "nation":"TW", "status":"1", "PID":"01000000"}
class EmployeeView(APIView):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        current_employee_count = Employee.objects.count()
        employee_number = current_employee_count
        EID = f"02{year}{month}{employee_number:04d}"
        if len(request.data) != 5:
            return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
        Employee.objects.create(
            EID=EID,
            name=request.data['name'],
            gender=request.data['gender'],
            phone=request.data['phone'],
            email=request.data['mail'],
            nation=request.data['nation'],
            status=3
        )
        return Response({'success': True, 'EID': EID}, status=status.HTTP_201_CREATED)
        
    def get(self, request, *args, **kwargs):
        EID = request.query_params.get('EID', None)
        nation = request.query_params.get('region', None)
        name = request.query_params.get('name', None)
        PID = request.query_params.get('PID', None)

        filters = Q()
        if EID:
            filters &= Q(EID=EID)
        if nation:
            filters &= Q(nation=nation)
        if name:
            filters &= Q(name__icontains=name)

        employees = Employee.objects.filter(filters)

        if PID:
            employees = employees.filter(EID__in=WorksOn.objects.filter(PID=PID).values_list('EID', flat=True))

        serializer = EmployeesSerialzer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # def put(self, request, EID, *args, **kwargs):
    def put(self, request, *args, **kwargs):
        eid = request.data.get('EID')
        # serializer = EmployeesSerialzer(employee, data=request.data)
        try:
            employee = Employee.objects.get(EID=eid)
        except Employee.DoesNotExist:
            return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
        
        # serializer = EmployeesSerialzer(employee, data=request.data)
        pid = request.data.get('PID', None)      
        if len(request.data) >= 6:
            Employee.objects.filter(EID=eid).update(
                name=request.data['name'],
                gender=request.data['gender'],
                phone=request.data['phone'],
                email=request.data['mail'],
                nation=request.data['nation'],
            )
            em = Employee.objects.filter(EID=eid)
            # new_data = EmployeesSerialzer(em)
            if pid:
                try:
                    employee = Employee.objects.get(EID=eid)
                    project = Project.objects.get(PID=pid)
                    # WorksOn.objects.create(EID=employee, PID=project, position="Default Position")
                except Project.DoesNotExist:
                    return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    
    
class DeleteEmployeeView(APIView):    
    def delete(self, request, *args, **kwargs):
        EID = request.query_params.get('EID')
        # name = request.query_params.get('name')

        # if not name:
        #     return Response({'error': 'Name is required to delete an employee'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # employee = Employee.objects.get(EID=EID, name=name)
            # # Update the status
            # employee.status = 0
            # employee.save()
            # WorksOn.objects.filter(EID=EID).delete()
            # user = User.objects.filter(username=name)
            # user.delete()
            # serializer = EmployeesSerialzer(employee)
            employee = Employee.objects.get(EID=EID)
            if employee.name != request.query_params.get('name'):
                return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
            employee.status = 0
            employee.save()
            Employee.objects.filter(EID=EID).update(
                status=0
            )
            # WorksOn.objects.filter(EID=EID).delete()
            user = User.objects.filter(username=employee.name)
            group, created = Group.objects.get_or_create(name='deleted')
            user.groups.clear()
            user.groups.add(group)
            return Response({'success': True}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
        

class GetAccessView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all().values('PID', 'pname')
        project_list = [{'id': project['PID'], 'name': project['pname']} for project in projects]
        return Response({'data': project_list}, status=status.HTTP_200_OK)

class GetBoundaryView(APIView):
    def get(self, request, *args, **kwargs):
        boundarys = Boundary.objects.all().values('BID', 'name')
        boundary_list = [{'bid': boundary['BID'], 'name': boundary['name']} for boundary in boundarys]
        return Response({'data': boundary_list}, status=status.HTTP_200_OK)