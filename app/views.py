from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import JsonResponse
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

        elif attempts > 1:
            ip = blocked_ip(sus_ips=get_ip(request))
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
        customers = Customer.objects.all()
        if request.user.is_superuser:
            return render(request, "home_auth.html", {
                'a': an,
                "user_details": UserJob.objects.get(username=request.user.username),
                "customers": customers,
                "todo": UserTodo.objects.filter(username=request.user.username)
            })
        else:
            return render(request, "home.html", {
                'a': an,
                "user_details": UserJob.objects.get(username=request.user.username),
                "customers": customers,
            })
    else:
        return render(request, "404.html")


def profitAPI(request):
    if request.user.is_authenticated & request.user.is_superuser:
        dictionary = {}
        for i in Earning.objects.all():
            dictionary[f"{i.day}"] = f"{int(i.revenue) - int(i.expense)}"

        return JsonResponse(dictionary)
    else:
        return render(request, "404.html")


def add_todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["todo_title"]
            due = request.POST["due_date"]
            remind = request.POST["remind_before"]

            todo = UserTodo(username=request.user.username, todo_title=title, due_at=due, remind_before_days=remind)
            todo.save()

            return redirect("/")
        else:
            return render(request, "add_todo.html")
    else:
        return render(request, "404.html")


def delete_todo(request, pk):
    UserTodo.objects.get(pk=pk).delete()
    return redirect("/")


def report(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            reported_user = request.POST["username"]
            reason = request.POST["reason"]

            html_message = f"""
<h1 style="color: red">Potential Threat</h1>
<p>SUSPECT: {reported_user} <br>
Reported by: {request.user.username} <br>
REASON: <br> 
{reason}</p>
  
            """

            for i in User.objects.filter(is_superuser=True):
                managment.send_mail(f"{i.username}", request, html_message, "", "Potential Threat")

            return redirect("/")

        else:
            return render(request, "report.html")
    else:
        return render(request, "404.html")
