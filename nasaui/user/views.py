from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# User = get_user_model()

"""
User reg and login 
"""


def register_view(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST.get('username'),
                                        request.POST.get('email'),
                                        request.POST.get('password'),
                                        first_name=request.POST.get('name'),
                                        last_name=request.POST.get('lastname'))

        user.save()
        return render(request, 'user/login.html')
    return render(request, 'user/register.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')  # redirect to index if login successful
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
