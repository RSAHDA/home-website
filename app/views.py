from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout
import managment

file = 'login.html'


def index(request):
    global file
    internal_file = file

    if internal_file == 'login.html':
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                file = 'home.html'
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
    elif internal_file == 'home.html':
        if request.method == 'POST':
            logout(request)
            file = "login.html"
            return render(request, "login.html")
        else:
            return render(request, "home.html")
