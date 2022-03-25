from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import *
import managment
import datetime

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
        due_todos = []

        # see if today is reminded day or due day for any UserTodo:
        for i in UserTodo.objects.filter(username=request.user.username):
            current_date = i.due_at
            if current_date.day == datetime.datetime.today().day and current_date.month == datetime.datetime.today().month and \
                    current_date.year == datetime.datetime.today().year:
                # today is due:
                due_todos.append(i)
            else:
                # check if today is reminded day:
                remind_date = i.due_at - datetime.timedelta(days=i.remind_before_days)
                if remind_date.day == datetime.datetime.today().day and remind_date.month == datetime.datetime.today().month and \
                        remind_date.year == datetime.datetime.today().year:
                    # today is reminded:
                    due_todos.append(i)

        if request.user.is_superuser:
            return render(request, "home_auth.html", {
                'a': an,
                "user_details": UserJob.objects.get(username=request.user.username),
                "customers": customers,
                "todo": UserTodo.objects.filter(username=request.user.username),
                "due_todos": due_todos,
            })
        else:
            return render(request, "home.html", {
                'a': an,
                "user_details": UserJob.objects.get(username=request.user.username),
                "customers": customers,
                "todo": UserTodo.objects.filter(username=request.user.username),
                "due_todos": due_todos,
            })
    else:
        return render(request, "404.html")


def profitAPI(request, salary):
    if request.user.is_authenticated:
        dictionary = {}
        if salary == 0:
            for i in Earning.objects.all():
                dictionary[f"{i.day}"] = f"{int(i.revenue) - int(i.expense)}"
        elif salary == 1:
            for i in UserJob.objects.all():
                dictionary[f"{i.job_title}"] = f"{i.salary}"

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

            if reported_user == "" or reason == "":
                return render(request, "report.html", {
                    "error": "All fields are required",
                })

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
