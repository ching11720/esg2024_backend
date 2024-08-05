from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# {test8 GVEh2HTJ}
class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            

    """
class revise_password(APIView):
    def revise_password(request):
        if request.method == 'POST':
            user = request.user
            old_password = request.POST['old_password']
            new_password1 = request.POST['new_password1']
            new_password2 = request.POST['new_password2']
            if user.check_password(old_password):
                user.set_password(new_password2)
                user.save()
                logout(request)
                message = 'Revised password successfully. Please log in again.'
                messages.success(request, message)
                return redirect('login')
                #update_session_auth_hash(request, form.user)
            else:
                message = 'Wrong password'
                messages.success(request, message)
                return redirect('revise_password')
        else:
            return render(request, 'revise_password.html')

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