from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .models import *
import managment

attempts = 0


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    global attempts
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        credentials = authenticate(username=username, password=password)

        if not managment.validateIP(get_ip(request)):
            return render(request, "404.html")

        elif credentials is not None:
            login(request, credentials)
            attempts = 0
            return redirect('/home')

<<<<<<< HEAD
        elif attempts > 3:
            ip = blocked_ip(sus_ips=managment.getIP())
=======
        elif attempts > 1:
            ip = blocked_ip(sus_ips=get_ip(request))
>>>>>>> 4d1d7be0d4f932bc2252a5327f49dcd395e2e8ae
            ip.save()
            return render(request, "404.html")

        else:
            attempts += 1
            return render(request, "login.html")

    else:
        if managment.validateIP(get_ip(request)) and request.user.is_authenticated:
            return redirect('/home')
        elif managment.validateIP(get_ip(request)):
            return render(request, "login.html")
        else:
            return render(request, "404.html")


def sign_out(request):
    logout(request)
    return redirect('/')


def home(request):
    if request.user.is_authenticated:

        an = Announcement.objects.all()
        return render(request, "home.html", {
            'a': an,
        })
    else:
        return render(request, "404.html")
