from django.shortcuts import render
from django.contrib.auth import authenticate
import managment


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
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
