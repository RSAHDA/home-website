from django.shortcuts import render, redirect
from django.contrib.auth import logout


def index(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/")
    else:
        if request.user.username != "":
            return render(request, "home.html")
        else:
            return redirect("/")
