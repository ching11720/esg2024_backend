from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from serializers import WorksOnSerializer
from pm.models import Employee, WorksOn
import hashlib

class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("user")
        password = request.data.get("password")
        # hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # user = authenticate(request, username=username, password=hashed)
        # user = User.objects.filter(username=username, password=hashed).first()
        # return Response(user)
        try:
            user= User.objects.get(username=username)
        except:
            return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
        # if user.check_password(hashed):
        if user.check_password(password):
        #if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            employee = Employee.objects.get(EID=username)
            if employee.status == 2:
                employee.status = 1
                employee.save()
                return Response({"success": True, "JWT": str(refresh.access_token), "first_login": True})
            else:
                return Response({"success": True, "JWT": str(refresh.access_token), "first_login": False})
        else:
            # return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)

# EID, Ename, authority, PM_rank    
class UserInfoView(APIView):
    def get(self, request, *args, **kwargs):
        uid = request.data.get("user")
        user = User.objects.get(username=uid)
        authority = user.groups.all()
        employee = Employee.objects.get(EID=uid)
        EName = employee.name
        worksons = WorksOn.filter(EID=employee)
        serializer = WorksOnSerializer(worksons, many=True)
        return Response({uid, EName, authority, serializer}, status=status.HTTP_200_OK)
    
class RevisePasswordView(APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # user = request.user
        uid = request.data.get('UID')
        old_password = request.data.get('old_password')
        # old_password = hashlib.sha256(old_password.encode('utf-8')).hexdigest()
        new_password = request.data.get('newPw')
        # new_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
        user = User.objects.get(username=uid)
        if not user.check_password(old_password): # frontend will check if the new passwords are the same
            return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()
        return Response({'success': True}, status=status.HTTP_200_OK)

    
    """
class CheckOldPasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        user = request.user
        old_password = request.data.get("old_password")
        if user.check_password(old_password):
            return Response('success', status=status.HTTP_200_OK)
        else:
            return Response({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)

class RevisePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    def put(self, request, *args, **kwargs):
        user = request.user
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        if new_password1 != new_password2:
                return Response({"new_password": "New passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password1)
        user.save()
        return Response({"success": "Password updated successfully"}, status=status.HTTP_200_OK)
        """
