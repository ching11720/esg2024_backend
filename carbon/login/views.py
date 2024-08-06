from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from admins.models import Employee


# {test8 GVEh2HTJ}
class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("user")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            """
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)"""
            return Response({'success': True, 'JWT': str(refresh.access_token), 'first_login': True})
        else:
            return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
            

    
class RevisePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # user = request.user
        uid = request.data.get('UID')
        old_password = request.data.get('old_password')
        new_password = request.data.get('newPw')
        em = Employee.objects.get(EID=uid)
        user = User.objects.get(username=em.name)
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