from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
import random, string, hashlib
from datetime import datetime
from .models import Employee
from django.db.models import Q

class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            permissions = serializer.validated_data['permission']
            try:
                employee = Employee.objects.get(name=username)
            except Employee.DoesNotExist:
                return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
            # user = User.objects.create_user(username=username, password=hashed)
            user = User(username=username)
            user.set_password(hashed)  # Set password plaintext; Django handles hashing
            user.save()
            if permissions:
                group = Group.objects.get(name=permissions)
                user.groups.add(group)
            return Response({'username': username, 'password': password, 'hashed': hashed}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class AssignAccessView(APIView):
    def put(self, request, *args, **kwargs):
        username = request.data.get('username')
        eid = request.data.get('userID')
        permissions = request.data.get('Access')
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
    
# {"pname":"project10", "PMID":"022024080009", "Material": "a, b", "Equipment": "c, d"}
class CreateProjectView(APIView):

    def post(self, request, *args, **kwargs):

        ms = request.data.get('Material')
        eqs = request.data.get('Equipment')

        # Get the current date
        now = datetime.now()
        yy = now.strftime("%y") 
        mm = now.strftime("%m")

        # Count the number of projects created in the current month
        current_month_projects = Project.objects.filter(PID__startswith=f"01{yy}{mm}").count()
        nn = current_month_projects + 1

        # Generate the PID
        PID = f"01{yy}{mm}{nn:02d}"

        # Add the generated PID to the request data
        request.data['PID'] = PID
        try:
            pmid = Employee.objects.get(EID=request.data.get('PMID'))
            #request.data['PMID'] = pmid
        except:
            return Response({'fail': 'PMID not found'}, status=status.HTTP_404_NOT_FOUND)
        project = Project.objects.create(PID=PID, pname=request.data.get('pname'), PMID=pmid)
        #serializer = ProjectSerializer(data=request.data)
        #if serializer.is_valid():
            #project = serializer.save()
            # Create an authentication group for the project
        group_name = f"project_{project.PID}"
        group = Group.objects.create(name=group_name)

        msl = ms.split(', ')
        eqsl = eqs.split(', ')
        for x in msl:
            usage = Usage.objects.create(PID=project, MID=x)
        for x in eqsl:
            usage = Usage.objects.create(PID=project, EQID=x)
        #return Response('success', status=status.HTTP_201_CREATED)
        return Response({'PID': PID, 'PMID': pmid.EID, 'Material': ms, 'Equipment': eqs}, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {"name":"test7", "gender":1, "phone":"0912345678", "email":"a@a.com", "nation":"TW", "status":"1", "PID":"01000000"}
class EmployeeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmployeesCreateSerialzer(data=request.data)
        pid = request.data.get('PID', None)
        if serializer.is_valid():
            # Generate EID in the format "02" + year + month + the number of the employee
            now = datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")

            # Get the current number of employees
            current_employee_count = Employee.objects.count()
            employee_number = current_employee_count + 1
            EID = f"02{year}{month}{employee_number:04d}"

            # Create employee
            Employee.objects.create(
                EID=EID,
                name=serializer.validated_data['name'],
                gender=serializer.validated_data['gender'],
                phone=serializer.validated_data['phone'],
                email=serializer.validated_data['email'],
                nation=serializer.validated_data['nation'],
                status=1
            )

            # works_on
            if pid:
                try:
                    employee = Employee.objects.get(EID=EID)
                    project = Project.objects.get(PID=pid)
                    WorksOn.objects.create(EID=employee, PID=project, position="Default Position")
                except Project.DoesNotExist:
                    return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

            return Response({'EID': EID, 'name': serializer.validated_data['name']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        EID = request.query_params.get('EID', None)
        nation = request.query_params.get('nation', None)
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


    def put(self, request, EID, *args, **kwargs):
        try:
            employee = Employee.objects.get(EID=EID)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
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
    
    
class DeleteEmployeeView(APIView):    
    def delete(self, request, *args, **kwargs):
        EID = request.query_params.get('EID')
        name = request.query_params.get('name')

        if not name:
            return Response({'error': 'Name is required to delete an employee'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            employee = Employee.objects.get(EID=EID, name=name)
            # Update the status
            employee.status = 0
            employee.save()
            WorksOn.objects.filter(EID=EID).delete()
            user = User.objects.filter(username=name)
            user.delete()
            serializer = EmployeesSerialzer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

"""
