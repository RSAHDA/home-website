# import django.contrib.auth
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import *
import managment

attempts = 0

blocked_ipx = []


def index(request):
    global attempts
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        credentials = authenticate(username=username, password=password)

        if credentials is not None:
            return render(request, "home.html")
        elif attempts > 3:
            ip = blocked_ip(sus_ips=managment.getIP())
            ip.save()
            return render(request, "404.html")
        else:
            attempts += 1
            return render(request, "login.html")

    else:
        if not managment.validateIP(managment.getIP()):
            return render(request, "login.html")
        else:
            return render(request, "404.html")
