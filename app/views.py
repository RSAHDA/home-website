# import django.contrib.auth
from django.shortcuts import render
from django.contrib.auth import authenticate
import managment

attempts = 5

blocked_ipx = []


def index(request):
    global attempts
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        credentials = authenticate(username=username, password=password)

        if credentials is not None:
            return render(request, "home.html")
        else:
            if managment.validateIP(managment.getIP()):
                return render(request, "login.html")
            else:
                return render(request, "404.html")
    else:
        if managment.validateIP(managment.getIP()):

            return render(request, "login.html")
        else:
            return render(request, "404.html")
