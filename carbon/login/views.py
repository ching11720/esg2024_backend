from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hello')
        else:
            messages.success(request, ("There is an error logging in."))
            return redirect('login')
    
    
    else:
        return render(request, 'loginpage.html')

    

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
def check_old_password(request):
    user = request.user
    old_password = request.POST['old_password']
    if user.check_password(old_password):
        return HttpResponse('true')
    else
        return HttpResponse('false')

def change_password(request):
    user = request.user
    new_password = request.POST['new_password']
    user.set_password(new_password)
    user.save()
"""